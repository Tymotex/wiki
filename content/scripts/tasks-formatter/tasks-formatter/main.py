import typer
from colorama import (
    init as init_colours,
    deinit as deinit_colours,
    Fore,
    Style
)

# TODO: moves these away
ARCHIVED_TASKS_FILENAME = "archived-tasks.md"
TASKS_FILENAME = "tasks.md"

class Board:
    def __init__(self, filename):
        self.board_file = open(filename, "r")
        self.frontmatter = {}
        self.tasks = []
        self.archived_tasks = []
        self.board_settings = {}

    @classmethod
    def create_task_file_if_note_exist():
        """
        Creates a new `archived-tasks.md` and `tasks.md` file with the source code
        necessary for a kanban board to be rendered by `obsidian-kanban`.
        """
        pass

    @classmethod
    def extract_board_data():
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

def normalise_file(f):
    # Strip all newlines.
    pass

def get_frontmatter(f):
    pass

def get_columns(f):
    pass

def get_archive(f):
    pass

def get_board_settings(f):
    pass

def main(num_future_dates: int = 30):
    create_task_files_if_not_exist()
    normalise_files()
    extract_board_data()

    print(Fore.GREEN + "Moving all previous tasks to today." + Style.RESET_ALL) 

    print(Fore.GREEN + f"Adding the next {num_future_dates} days" + Style.RESET_ALL)

if __name__ == "__main__":
    try:
        # Makes coloured printing cross-platform. See: https://pypi.org/project/colorama/.
        init_colours()
        print(Fore.BLUE + " ✓ Formatting Tasks" + Style.RESET_ALL)
        typer.run(main)
    finally:
        # Restore output streams to original values.
        deinit_colours()
