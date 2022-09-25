import typer
import os
from colorama import Fore, Style
from colorama import deinit as deinit_colours
from colorama import init as init_colours

from tasks_formatter.task_manager import TaskManager


def main(tasks_file_path: str, archived_tasks_file_path: str, num_future_dates: int = 30):
    if not os.path.exists(archived_tasks_file_path):
        print(Fore.RED + f"Archived tasks file '{archived_tasks_file_path}' does not exist." + Style.RESET_ALL)
        return
    if not os.path.exists(tasks_file_path):
        print(Fore.RED + f"Tasks file '{tasks_file_path}' does not exist." + Style.RESET_ALL)
        return

    print(Fore.GREEN + f" → Using tasks file: {tasks_file_path}." + Style.RESET_ALL) 
    print(Fore.GREEN + f" → Using archived tasks file: {archived_tasks_file_path}." + Style.RESET_ALL) 
    print(Fore.GREEN + f" → Moving all previous tasks to today and adding the next {num_future_dates} days." + Style.RESET_ALL) 
    task_manager = TaskManager(archived_tasks_file_path, tasks_file_path)

    task_manager.format(num_future_dates)
    print(Fore.GREEN + f" → Done formatting. ✨" + Style.RESET_ALL) 

if __name__ == "__main__":
    try:
        # Makes coloured printing cross-platform. See: https://pypi.org/project/colorama/.
        init_colours()
        print(Fore.BLUE + "Formatting Tasks..." + Style.RESET_ALL)
        typer.run(main)
    finally:
        # Restore output streams to original values.
        deinit_colours()
