from scripts.tasks-formatter.tasks_formatter.exceptions import TemplateFileException
from scripts.tasks-formatter.tasks_formatter.exceptions import TaskFileException
import typer
import os
from colorama import Fore, Style
from colorama import deinit as deinit_colours
from colorama import init as init_colours

from tasks_formatter.task_manager import TaskManager
from journal_templater.journal_manager import JournalManager
from journal_templater.exceptions import JournalException

def format_tasks(tasks_file_path: str, archived_tasks_file_path: str, num_future_dates: int) -> None:
    if not os.path.exists(archived_tasks_file_path):
        print(Fore.RED + f"Archived tasks file '{archived_tasks_file_path}' does not exist." + Style.RESET_ALL)
        return
    if not os.path.exists(tasks_file_path):
        print(Fore.RED + f"Tasks file '{tasks_file_path}' does not exist." + Style.RESET_ALL)
        return

    try:
        print(Fore.GREEN + f" → Using tasks file: {tasks_file_path}." + Style.RESET_ALL) 
        print(Fore.GREEN + f" → Using archived tasks file: {archived_tasks_file_path}." + Style.RESET_ALL) 
        print(Fore.GREEN + f" → Moving all previous tasks to today and adding the next {num_future_dates} days." + Style.RESET_ALL) 
        task_manager = TaskManager(archived_tasks_file_path, tasks_file_path)

        task_manager.format(num_future_dates)
        print(Fore.GREEN + f" → Done formatting. ✨" + Style.RESET_ALL) 
    except TaskFileException as err:
        print(Fore.RED + f"❌ Error with task file: {err}" + Style.RESET_ALL)
    except TemplateFileException as err:
        print(Fore.RED + f"❌ Error with task template files: {err}" + Style.RESET_ALL)

def generate_journal_entries(journal_directory_path: str, journal_template_file_path: str, journal_variables_file_path: str, num_future_dates: int) -> None:
    try:
        journal_manager = JournalManager(journal_directory_path, journal_template_file_path, journal_variables_file_path)
        journal_manager.archive_old_entries(0)
        print(Fore.GREEN + f" → Done archiving older journal entries." + Style.RESET_ALL) 
        journal_manager.create_journal_entries(num_future_dates)
        print(Fore.GREEN + f" → Done generating journal entries. ✨" + Style.RESET_ALL) 
    except JournalException as err:
        print(Fore.RED + f"❌ Error with journals: {err}" + Style.RESET_ALL)

def main(tasks_file_path: str, archived_tasks_file_path: str,
        journal_directory_path: str, journal_template_file_path: str,
        journal_variables_file_path: str, num_future_dates: int = 7):
    print(Fore.BLUE + "Formatting Tasks..." + Style.RESET_ALL)
    format_tasks(tasks_file_path, archived_tasks_file_path, num_future_dates)

    print(Fore.BLUE + "Generating Journal Entries..." + Style.RESET_ALL)
    generate_journal_entries(journal_directory_path, journal_template_file_path,
        journal_variables_file_path, num_future_dates)

if __name__ == "__main__":
    try:
        # Makes coloured printing cross-platform. See: https://pypi.org/project/colorama/.
        init_colours()
        typer.run(main)
    finally:
        # Restore output streams to original values.
        deinit_colours()
