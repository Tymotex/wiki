import typer
from tasks_formatter.board import BoardManager
from colorama import (
    init as init_colours,
    deinit as deinit_colours,
    Fore,
    Style
)

# TODO: moves these away
ARCHIVED_TASKS_FILENAME = "archived-tasks.md"
TASKS_FILENAME = "tasks.md"

def main(num_future_dates: int = 30):
    # board: Board = Board(TASKS_FILENAME)

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
