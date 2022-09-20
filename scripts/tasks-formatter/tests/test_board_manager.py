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

def test_remove_up_to_date():
    test_file_path = get_task_file_path("valid_1.md")
    task_file_manager = TaskFileManager(test_file_path)

    tasks = task_file_manager.remove_tasks_up_to_date(datetime(year=2022, month=9, day=21))
    assert(tasks == [
        (datetime(year=2022, month=9, day=19), [
            "- [ ] 🏆 **Purpose today**: get chores done",
            "- [ ] **(2 hours)** Refine and review C++ notes #critical",
            "- [x] [[_/(1 hour)  Set up git sync with mobile.]]"
        ]),
        (datetime(year=2022, month=9, day=20), [
            "- [ ] Go to CPMSoc event.",
        ]),
    ])

def test_remove_up_to_date_all():
    test_file_path = get_task_file_path("valid_1.md")
    task_file_manager = TaskFileManager(test_file_path)

    tasks = task_file_manager.remove_tasks_up_to_date(datetime(year=2022, month=9, day=30))
    assert(tasks == [
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

def test_remove_up_to_date_none():
    test_file_path = get_task_file_path("valid_1.md")
    task_file_manager = TaskFileManager(test_file_path)

    tasks = task_file_manager.remove_tasks_up_to_date(datetime(year=2022, month=8, day=10))
    assert(tasks == [])

def test_append_tasks():
    test_file_path = get_task_file_path("valid_1.md")
    task_file_manager = TaskFileManager(test_file_path)

    new_tasks = [
        (datetime(year=2022, month=9, day=26), [
            "- [ ] Buy new noise-cancelling headphones.",
        ]),
        (datetime(year=2022, month=9, day=27), [
            "- [x] Sort music playlist.",
        ]),
        (datetime(year=2022, month=9, day=29), [
            "- [] Migrate from Notion to Obsidian.",
        ]),
        (datetime(year=2022, month=10, day=4), [
            "- [ ] Reinstall Arch Linux.",
        ]),
    ]
    task_file_manager.insert_task_columns(new_tasks)

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
    ] + new_tasks)

def test_append_tasks_empty():
    test_file_path = get_task_file_path("valid_1.md")
    task_file_manager = TaskFileManager(test_file_path)

    task_file_manager.insert_task_columns([])
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

def test_search_for_task_date():
    test_file_path = get_task_file_path("valid_1.md")
    task_file_manager = TaskFileManager(test_file_path)

    # Hit.
    index = task_file_manager._search_for_task_date(0, 6, datetime(year=2022, month=9, day=21))
    assert(index == 2)

    # No hit.
    index = task_file_manager._search_for_task_date(0, 6, datetime(year=2022, month=9, day=1))
    assert(index == 0)
    index = task_file_manager._search_for_task_date(0, 6, datetime(year=2022, month=9, day=29))
    assert(index == 7)

# TODO: exception throwing tests.
