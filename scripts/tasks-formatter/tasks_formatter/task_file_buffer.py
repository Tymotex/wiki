import os
from pprint import pprint
import re
from asyncio import Task
from datetime import datetime, timedelta
from io import TextIOWrapper
from typing import List, Set, Tuple, Union

from colorama import Fore, Style

from tasks_formatter.exceptions import TaskFileException, TemplateFileException

TEMPLATES_DIRECTORY = os.path.join(os.path.dirname(__file__), "templates")

class TaskFileBuffer:
    level2_heading_regex = re.compile(r"^## (.*)$")

    # Examples of what this regex pattern matches:
    # 1. `- []`
    # 2. `- [x] Hello world`
    # 3. `- [ ] ==42== **(10 mins)** Start reading that book.`
    # Capture groups match for whether the box is checked, the number of times
    # the card has shifted forward, and the actual task description.
    # Why track the number of times a card shifts forward? To discourage tasks 
    # from constantly shifting forward... ie. identify and prevent
    # procrastination.
    checkbox_regex = re.compile(r"^-\s*\[(\s*|\S+)\] ?(==\d+==)?(.*)$")
    
    # Every column should have a date in the universal ISO format,
    # eg. 2022-09-20.
    column_name_date_regex = re.compile(r"(\d{4}-\d{2}-\d{2})")

    def __init__(self, task_file_path: str) -> None:
        self._task_file_path: str = task_file_path
        self._frontmatter: str = ""
        self._tasks: List[Tuple[datetime, List[str]]] = []
        self._archived_tasks: List[str] = []
        self._task_settings: str = ""

        self._extract_board_data()

    @property
    def frontmatter(self):
        return self._frontmatter

    @property
    def tasks(self):
        return self._tasks

    @property
    def archived_tasks(self):
        return self._archived_tasks

    def remove_tasks_up_to_date(self, date: datetime) -> List[Tuple[datetime, List[str]]]:
        """
        Sorts and slices out a list of tasks in `self._tasks` up to, but not
        including, the given date.
        """
        # Sort by date before slicing.
        self._tasks.sort(key=lambda task: task[0])

        date_index = self._search_for_task_date(0, len(self._tasks) - 1, date)
        removed_tasks = self._tasks[0 : date_index]

        self._tasks = self._tasks[date_index :]
        return removed_tasks

    def insert_task_columns(self, task_columns: List[Tuple[datetime, List[str]]]) -> None:
        """
        Adds the given tasks and sorts them by date.
        """
        for date, tasks in task_columns:
            # Check all tasks in this column are valid.
            for task in tasks:
                if not TaskFileBuffer.checkbox_regex.search(task):
                    raise TaskFileException(f"Attempted to insert invalid task: '{task}'")
        self._tasks.extend(task_columns)

        # Sort by date.
        self._tasks.sort(key=lambda task: task[0])

    def shift_incomplete_tasks_to_date(self, date: datetime) -> None:
        """
        Moves all incomplete non-archived tasks before today to today's task
        column.
        """
        # Sort task columns by date before slicing.
        self._tasks.sort(key=lambda task: task[0])

        date_index = self._search_for_task_date(0, len(self._tasks) - 1, date)

        # A list of incomplete tasks and the number of times they've been
        # shifted forward. 
        incomplete_tasks_from_prev_days: List[str] = []

        curr_date_index = 0
        for _, tasks in self._tasks[0 : date_index]:
            # Note: need to create a new list of tasks to not invalidate tasks
            #       we remove as we iterate.
            for task in list(tasks):
                match = TaskFileBuffer.checkbox_regex.search(task) 
                if not match:
                    raise TaskFileException(f"Invalid task: {task}")
                checked = not match.group(1).isspace()

                # Record the incomplete tasks and take them off the task column
                # of previous days.
                if not checked:
                    # Reconstruct the task so that we can etch the number of
                    # times this card moved forward into the task string.
                    # Note: the syntax ==Hi== is part of Obsidian's markdown
                    #       which highlights the text 'Hi'.
                    num_days_from_target_date = date_index - curr_date_index
                    times_shifted = (int(match.group(2).strip("=")) if match.group(2) else 0) + num_days_from_target_date
                    task_description = match.group(3)
                    reconstructed_task = f"- [{'X' if checked else ' '}] =={times_shifted}==\n{task_description.strip()}"
                    incomplete_tasks_from_prev_days.append(reconstructed_task)
                    tasks.remove(task)

            curr_date_index += 1

        if len(self._tasks) == 0 or self._tasks[date_index][0] != date:
            # Add today into the task file. Note: this is unexpected, today's
            # task column should already exist.
            self.insert_task_columns([(date, incomplete_tasks_from_prev_days)])
        else:
            # Insert all incomplete tasks to today's column.
            self._tasks[date_index][1].extend(incomplete_tasks_from_prev_days)

    def add_columns_up_to_date(self, start_date: datetime, end_date: datetime) -> None:
        """
        Inserts empty columns for each date up to and including the given date.
        If a date's column already exists, then don't do anything to that
        column.
        """
        new_task_columns: List[Tuple[datetime, List[str]]] = []
        
        # All the dates we have so far in the task buffer.
        task_dates: Set[datetime] = { date for date, _ in self._tasks }

        one_day = timedelta(days=1)
        curr_date = start_date
        while curr_date <= end_date:
            if curr_date not in task_dates:
                new_task_columns.append((curr_date, self._get_default_tasks(curr_date)))
            curr_date += one_day
        self.insert_task_columns(new_task_columns)

    def commit_changes(self, reverse: bool = False):
        """
        Writes the state of the task file buffer instance into the task file.
        """
        with open(self._task_file_path, "w") as task_file:
            # Write in the frontmatter.
            task_file.write(self._frontmatter + "\n\n")

            # Write in the tasks.
            # Note: obsidian-kanban uses (n) to determine how many cards should
            #       go into a column. Here, we chose (6) because that's the
            #       number that the Ivy Lee method uses.
            tasks = self._tasks if not reverse else reversed(self._tasks)
            for date, tasks in self._tasks:
                # Every column's name is clickable and links to that date's
                # daily note.
                universal_iso_date = date.strftime('%Y-%m-%d')
                column_name = f"## **{date.strftime('%A')}** *[[Journal/{universal_iso_date}|{universal_iso_date}]]* (6)\n\n"
                task_file.write(column_name)
                task_file.writelines("\n".join(tasks) + "\n\n")

            # Write in the archived tasks.
            task_file.write("***\n\n")
            column_name = "## Archive\n\n"
            task_file.write(column_name)
            task_file.writelines("\n".join(self._archived_tasks) + "\n\n")

            # Write in the board settings.
            task_file.write(self._task_settings)
    
    def _extract_board_data(self) -> None:
        """
        Reads the board file, stepping through each line and extracting out all
        the data such as the frontmatter, current tasks, etc.

        Throws an error if either of the tasks file is invalid. Expects both
        files to have been normalised with `normalise_files`.

        From top to bottom, the expected structure of the file should follow the
        given rules:
        1. Must have the frontmatter field: `kanban-plugin: .*`.
        2. 0 or more level-2 headings follow. For each of them, they are followed
        by 0 or more markdown checkboxes and empty lines.
        3. Markdown divider (*** or --- or ___).
        4. Level-2 heading '## Archive' followed by 0 or more markdown checkboxes
        and empty lines.
        5. Kanban settings comment block which looks like this:
            %% kanban:settings
            ```
            {"kanban-plugin":".*"}
            ```
            %%
        6. End of file.
        """
        with open(self._task_file_path, "r") as task_file:
            # Get all non-empty lines of the file and sequentially identify and
            # extract the data of each relevant section of the task file.
            lines: List[str] = [line.strip() for line in task_file.readlines() if bool(re.match(r"\S+", line))]
            resume_line_index = self._extract_frontmatter(lines)
            resume_line_index = self._extract_columns(lines, resume_line_index)
            resume_line_index = self._extract_archive(lines, resume_line_index)
            self._extract_board_settings(lines, resume_line_index)

    def _extract_frontmatter(self, lines, starting_line: int = 0) -> int: 
        """
        NOTE: This function should be called first when parsing the task file.

        Extracts the YAML frontmatter from the task file and dumps it to 
        `self.frontmatter`.
        """
        if len(lines) < 3:
            raise TaskFileException("File does not have a complete YAML frontmatter block.")
        if lines[0] != "---":
            raise TaskFileException("File must start with --- to begin YAML frontmatter block.")

        has_kanban_field = False
        for i in range(starting_line + 1, len(lines)):
            curr_line = lines[i]

            # End of frontmatter.
            if curr_line == "---":
                if not has_kanban_field:
                    raise TaskFileException("No 'kanban-plugin' field specified.") 
                self._frontmatter = "\n".join(lines[starting_line : i + 1])
                return i + 1
            
            # The field must follow a valid format.
            if not bool(re.match(r"^[-a-zA-Z0-9]+: .+$", curr_line)):
                raise TaskFileException(f"Invalid frontmatter field: '{curr_line}'")
            if bool(re.match(r"^kanban-plugin: .*$", curr_line)):
                if has_kanban_field:
                    raise TaskFileException("Frontmatter field 'kanban-plugin' appeared more than once.")
                has_kanban_field = True   
        
        raise TaskFileException("No ending YAML frontmatter delimiter encountered.")

    def _extract_columns(self, lines: List[str], starting_line: int) -> int:
        """
        NOTE: This function must be called after `_extract_frontmatter`.

        After the frontmatter has been parsed, we expect a sequence of 0 or 
        more level-2 headings, stopping when a divider is encountered.

        Extracts the columns and their tasks and saves it to `self.tasks`.
        """
        if starting_line >= len(lines):
            return starting_line

        curr_column: Union[Tuple[datetime, List[str]], None] = None
        for i in range(starting_line, len(lines)):
            curr_line = lines[i]

            # Stop when a Markdown horizontal rule is encountered.
            if curr_line == "---" or curr_line == "___" or curr_line == "***":
                # Commit the final task column.
                if curr_column:
                    self._tasks.append(curr_column)
                return i + 1

            match = TaskFileBuffer.level2_heading_regex.search(curr_line)
            if match:
                # Commit the last column of tasks before extracting tasks from
                # the new column.
                if curr_column:
                    self._tasks.append(curr_column)
                column_name = match.group(1)
                match = TaskFileBuffer.column_name_date_regex.search(column_name)
                if not match:
                    raise TaskFileException("Column '{column_name}' is missing a date of format: YYYY-MM-DD.")
                date_str = match.group(1)
                curr_column = (datetime.strptime(date_str, "%Y-%m-%d"), [])
            else:
                match = TaskFileBuffer.checkbox_regex.search(curr_line)
                if match:
                    if not curr_column:
                        raise TaskFileException(f"Line '{curr_line}' doesn't belong to any column.")
                    curr_column[1].append(curr_line)
                else:
                    raise TaskFileException(f"Line '{curr_line}' is neither a level-2 heading nor a Markdown checkbox.")

        raise TaskFileException("No ending Markdown divider encountered.")

    def _extract_archive(self, lines: List[str], starting_line: int) -> int:
        """
        NOTE: This function must be called after `_extract_columns`.

        After the frontmatter and task columns have been parsed, we expect
        a sequence of checkboxes, stopping when a comment block with '%%' is
        encountered.

        Extracts the archived tasks and saves it to `self.archived_tasks`.
        """
        if starting_line >= len(lines):
            return starting_line

        match = TaskFileBuffer.level2_heading_regex.search(lines[starting_line])
        if not match or match.group(1) != "Archive":
            raise TaskFileException(f"Expected the level 2 heading with text 'Archive' but got '{lines[starting_line]}'")

        for i in range(starting_line + 1, len(lines)):
            curr_line = lines[i]

            # Stop when '%%' is encountered, which signals the start of the
            # settings comment block.
            if curr_line.startswith("%%"):
                return i + 1

            match = TaskFileBuffer.checkbox_regex.search(curr_line)
            if not match:
                raise TaskFileException(f"Line '{curr_line}' should be a Markdown checkbox.")

            self._archived_tasks.append(curr_line) 
        raise TaskFileException("Expected settings comment block, delimited by '%%'.")

    def _extract_board_settings(self, lines: List[str], starting_line: int) -> int:
        """
        NOTE: This function must be called after `_extract_archive`.

        After everything else in the task file has been parsed, we expect the
        end of the comment block when we see the closing '%%'.

        Extracts the board settings and saves it to `self.board_settings`.
        """
        if starting_line >= len(lines):
            return starting_line

        board_settings = "%% kanban:settings\n"
        for i in range(starting_line, len(lines)):
            curr_line = lines[i]
            board_settings += curr_line + "\n"
            # Stop when '%%' is encountered, which signals the end of the
            # settings comment block.
            if curr_line == "%%":
                self._task_settings = board_settings
                return i + 1
        raise TaskFileException("Expected ending of settings comment block, delimited by '%%'.")

    def _search_for_task_date(self, low: int, high: int, target: datetime):
        """
        Binary searches for the given target date in the tasks. If it's found
        return its index, otherwise, return the index where we expect to find
        it, if it were to exist.
        """
        while low <= high:
            mid = low + (high - low)//2
            if self._tasks[mid][0] == target:
                return mid
            elif self._tasks[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def _get_tasks_from_templates(self, *template_filenames: str) -> List[str]:
        """
        Reads the lines from the given template file, expecting them as
        markdown checkboxes, and returns them as a list of tasks.
        The main use case for this is to allow a default set of tasks to be
        added to each day's lane.
        """
        tasks: List[str] = []
        for template_filename in template_filenames:
            template_file_path = os.path.join(TEMPLATES_DIRECTORY, template_filename)
            if not os.path.exists(template_file_path):
                raise TemplateFileException(f"Template file at path '{template_file_path}' does not exist.")
            with open(template_file_path, "r") as template_file:
                template_tasks = [line.strip() for line in template_file.readlines() if line and not line.isspace()]
                for task in template_tasks:
                    if not TaskFileBuffer.checkbox_regex.search(task):
                        raise TemplateFileException(f"Invalid task in template file: '{task}'")
                    tasks.append(task)
        return tasks

    def _get_default_tasks(self, date: datetime) -> List[str]:
        """
        Returns a list of default tasks that should be scheduled on the date.
        For example, each day might have a morning routine task.
        - For all days, schedule a basic set of daily default tasks sourced from
          `templates/daily.md`.
        - If the date is a Sunday, then schedule a set of weekly tasks sourced
          from `templates/weekly.md`.
        - If the date is the last day of the month, then schedule a set of
          monthly tasks sourced from `templates/monthly.md`.
        
        Note: This could have been implemented in a much less rigid way, but
              I wanted to just get this done ASAP.
        """
        # List of template files whose tasks we want to schedule for the day.
        template_files: List[str] = []

        # Always schedule daily tasks.
        template_files.append("daily.md")

        # On Sundays, schedule weekly tasks.
        if date.weekday() == 6:
            template_files.append("weekly.md")

        # On last day of the month, schedule monthly tasks.
        todays_month = date.month
        tomorrows_month = (date + timedelta(days=1)).month
        is_last_day_of_month = tomorrows_month != todays_month
        if is_last_day_of_month:
            template_files.append("monthly.md")
    
        return self._get_tasks_from_templates(*template_files)
