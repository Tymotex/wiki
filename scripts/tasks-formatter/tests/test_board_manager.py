from datetime import datetime
import os
from pprint import pprint
from tasks_formatter.task_file_manager import TaskFileManager

TEST_TASK_FILE_DIRECTORY = os.path.join(os.path.dirname(__file__), "task_files")

def get_task_file_path(filename: str):
    test_file_path = os.path.join(TEST_TASK_FILE_DIRECTORY, filename)
    assert(os.path.exists(test_file_path))
    return test_file_path

def test_valid_task_file_extraction():
    test_file_path = get_task_file_path("valid_1.md")
    task_file_manager = TaskFileManager(test_file_path)
    
    # Check frontmatter identified and extracted successfully.
    assert(task_file_manager.frontmatter == "\n".join(["---", "kanban-plugin: basic", "---"]))
    
    # Check tasks identified and extracted successfully.
    assert(task_file_manager.tasks == [
        (datetime(year=2022, month=9, day=19), [
            "- [ ] 🏆 **Purpose today**: get chores done",
            "- [ ] **(2 hours)** Refine and review C++ notes #critical",
            "- [x] [[_/(1 hour)  Set up git sync with mobile.]]"
        ]),
        (datetime(year=2022, month=9, day=20), [
            "- [ ] Go to CPMSoc event.",
        ]),
        (datetime(year=2022, month=9, day=21), [
            "- [ ] Go to CSESoc event.",
            "- [ ] **(1 hour)** Figma prototype."
        ]),
        (datetime(year=2022, month=9, day=22), [
            "- [x] Install Linux VM on laptop, then VSCode with settings synced.",
        ]),
        (datetime(year=2022, month=9, day=23), []),
        (datetime(year=2022, month=9, day=24), []),
        (datetime(year=2022, month=9, day=25), [])
    ])

def test_valid_empty_task_file():
    test_file_path = get_task_file_path("valid_empty.md")
    task_file_manager = TaskFileManager(test_file_path)

    # Check frontmatter identified and extracted successfully.
    assert(task_file_manager.frontmatter == "\n".join(["---", "kanban-plugin: basic", "---"]))

    # Check that tasks have not been populated.
    assert(len(task_file_manager.tasks) == 0)
    assert(len(task_file_manager.archived_tasks) == 0)

def test_valid_no_tasks_listed():
    test_file_path = get_task_file_path("valid_empty_tasks.md")
    task_file_manager = TaskFileManager(test_file_path)

    # Check frontmatter identified and extracted successfully.
    assert(task_file_manager.frontmatter == "\n".join(["---", "kanban-plugin: basic", "---"]))

    # Check that tasks have not been populated.
    assert(len(task_file_manager.tasks) == 0)
    assert(len(task_file_manager.archived_tasks) == 1)

# TODO: exception throwing tests.
