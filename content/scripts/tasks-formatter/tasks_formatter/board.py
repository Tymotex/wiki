from io import TextIOWrapper
import os
from colorama import Fore, Style

class Board:
    def __init__(self, task_file_path):
        self.create_task_file_if_not_exist(task_file_path)

        self.task_file_path = task_file_path
        self.frontmatter = {}
        self.tasks = []
        self.archived_tasks = []
        self.board_settings = {}

        self._extract_board_data()

    def create_task_file_if_not_exist(self, task_file_path: str):
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
        with open(self.task_file_path, "r") as task_file:
            for line in task_file:
                print(line)

    def _extract_frontmatter(self, task_file: TextIOWrapper):
        pass

    def _extract_columns(self):
        pass

    def _extract_archive(self):
        pass

    def _extract_board_settings(self):
        pass
