from asyncio import Task
from datetime import datetime
from io import TextIOWrapper
import os
import re
from tabnanny import check
from typing import List, Tuple, Union
from colorama import Fore, Style

class TaskFileException(Exception):
    pass

class BoardManager:
    level2_heading_regex = re.compile(r"^## (\w+)")
    checkbox_regex = re.compile(r"^-\s*\[(\s+|\S+)\] (.*)$")
    
    # Every column should have a date in the universal ISO format,
    # eg. 2022-09-20.
    column_name_date_regex = re.compile(r"(\d{4}-\d{2}-\d{2})")

    def __init__(self, task_file_path: str):
        self._create_task_file_if_not_exist(task_file_path)

        self._task_file_path: str = task_file_path
        self._frontmatter: str = ""
        self._tasks: List[Tuple[datetime, List[str]]] = []
        self._archived_tasks: List[str] = []
        self._board_settings: str = ""

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

    def remove_tasks_up_to_date(self, date: datetime) -> List[Tuple[str, List[str]]]:
        """
        Sorts and slices out a list of tasks in `self._tasks` up to, but not
        including, the given date.
        """
        self._tasks.sort(key=lambda task: task[0])
        return []

    def _create_task_file_if_not_exist(self, task_file_path: str):
        """
        Creates a new task file with the source code necessary for a kanban
        board to be rendered by `obsidian-kanban`.
        """
        directory_path, filename = task_file_path.rsplit(os.sep, 1)
        if not os.path.exists(directory_path):
            print(Fore.CYAN + f" → Creating directory: {directory_path}" + Style.RESET_ALL)
            os.makedirs(directory_path)
        if not os.path.exists(task_file_path):
            print(Fore.CYAN + f" → Creating task file: {filename}" + Style.RESET_ALL)
            open(task_file_path, "a").close()
    
    def _extract_board_data(self):
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
        task_file = open(self._task_file_path, "r")

        # Get all non-empty lines of the file and sequentially identify and
        # extract the data of each relevant section of the task file.
        lines: List[str] = [line for line in task_file.readlines() if bool(re.match(r"\S+", line))]
        resume_line_index = self._extract_frontmatter(lines)
        resume_line_index = self._extract_columns(lines, resume_line_index)
        resume_line_index = self._extract_archive(lines, resume_line_index)
        self._extract_archive(lines, resume_line_index)

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
            
            # The field must follow a valid format.
            if not bool(re.match(r"^\w: .+$", curr_line)):
                raise TaskFileException(f"Invalid frontmatter field: '{curr_line}'")
            if bool(re.match(r"^kanban-plugin: .*$", curr_line)):
                if has_kanban_field:
                    raise TaskFileException("Frontmatter field 'kanban-plugin' appeared more than once.")
                has_kanban_field = True
            
            # End of frontmatter.
            if curr_line == "---":
                if not has_kanban_field:
                    raise TaskFileException("No 'kanban-plugin' field specified.") 
                self._frontmatter = "\n".join(lines[starting_line : i + 1])
                return i + 1
        
        raise TaskFileException("No ending YAML frontmatter delimiter encountered.")

    def _extract_columns(self, lines: List[str], starting_line: int) -> int:
        """
        NOTE: This function must be called after `_extract_frontmatter`.

        After the frontmatter has been parsed, we expect a sequence of 0 or 
        more level-2 headings, stopping when a divider is encountered.

        Extracts the columns and their tasks and saves it to `self.tasks`.
        """
        if starting_line >= len(lines):
            raise TaskFileException("Tasks section is missing.")

        curr_column: Union[Tuple[datetime, List[str]], None] = None
        for i in range(starting_line, len(lines)):
            curr_line = lines[i]
            # Stop when a Markdown horizontal rule is encountered.
            if curr_line == "---" or curr_line == "___" or curr_line == "***":
                return i + 1

            match = BoardManager.level2_heading_regex.search(curr_line)
            if match:
                # Commit the last column of tasks into `self.tasks` before
                # extracting tasks from the new column.
                if curr_column:
                    self._tasks.append(curr_column)
                column_name = match.group(1)
                match = BoardManager.column_name_date_regex.search(column_name)
                if not match:
                    raise TaskFileException("Column '{column_name}' is missing a date of format: YYYY-MM-DD.")
                date_str = match.group(1)
                curr_column = (datetime.strptime(date_str, "%Y-%m-%d"), [])
            else:
                match = BoardManager.checkbox_regex.search(curr_line)
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
            raise TaskFileException("Archived tasks section is missing.")

        match = BoardManager.level2_heading_regex.search(lines[starting_line])
        if not match or match.group(1) != "Archive":
            raise TaskFileException("Expected the level 2 heading with text 'Archive'.")

        for i in range(starting_line + 1, len(lines)):
            curr_line = lines[i]

            # Stop when '%%' is encountered, which signals the start of the
            # settings comment block.
            if curr_line == "%%":
                return i + 1

            match = BoardManager.checkbox_regex.search(curr_line)
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
            raise TaskFileException("Tasks settings section is missing.")

        board_settings = "%%"
        for i in range(starting_line, len(lines)):
            curr_line = lines[i]
            board_settings += curr_line
            # Stop when '%%' is encountered, which signals the end of the
            # settings comment block.
            if curr_line == "%%":
                self._board_settings = board_settings
                return i + 1
        raise TaskFileException("Expected ending of settings comment block, delimited by '%%'.")
