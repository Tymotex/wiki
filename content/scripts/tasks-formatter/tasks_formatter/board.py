class Board:
    def __init__(self, filename):
        self.board_file = open(filename, "r")
        self.frontmatter = {}
        self.tasks = []
        self.archived_tasks = []
        self.board_settings = {}
        self._extract_board_data()

    def create_task_file_if_not_exist(self):
        """
        Creates a new task file with the source code necessary for a kanban
        board to be rendered by `obsidian-kanban`.
        """
        pass

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
        pass

    def _normalise_task_file(self):
        # Strip all newlines.
        pass

    def _extract_frontmatter(self):
        pass

    def _extract_columns(self):
        pass

    def _extract_archive(self):
        pass

    def _extract_board_settings(self):
        pass
