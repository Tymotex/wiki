from datetime import datetime
import os
import pytest
from tasks_formatter.exceptions import TaskFileException, TemplateFileException
from tasks_formatter.task_file_buffer import TaskFileBuffer

TEST_TASK_FILE_DIRECTORY = os.path.join(os.path.dirname(__file__), "task_files")
TEMPLATE_FILE_DIRECTORY = os.path.join(os.path.dirname(__file__), "templates")

def get_test_file_path(filename: str, directory=TEST_TASK_FILE_DIRECTORY):
    test_file_path = os.path.join(directory, filename)
    assert(os.path.exists(test_file_path))
    return test_file_path

def test_valid_task_file_extraction():
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)
    
    # Check frontmatter identified and extracted successfully.
    assert(task_file_buffer.frontmatter == "\n".join(["---", "kanban-plugin: basic", "---"]))
    
    # Check tasks identified and extracted successfully.
    assert(task_file_buffer.tasks == [
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
    test_file_path = get_test_file_path("valid_empty.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    # Check frontmatter identified and extracted successfully.
    assert(task_file_buffer.frontmatter == "\n".join(["---", "kanban-plugin: basic", "---"]))

    # Check that tasks have not been populated.
    assert(len(task_file_buffer.tasks) == 0)
    assert(len(task_file_buffer.archived_tasks) == 0)

def test_valid_no_tasks_listed():
    test_file_path = get_test_file_path("valid_empty_tasks.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    # Check frontmatter identified and extracted successfully.
    assert(task_file_buffer.frontmatter == "\n".join(["---", "kanban-plugin: basic", "---"]))

    # Check that tasks have not been populated.
    assert(len(task_file_buffer.tasks) == 0)
    assert(len(task_file_buffer.archived_tasks) == 1)

def test_missing_frontmatter():
    with pytest.raises(TaskFileException):
        task_file_path = get_test_file_path("invalid_1.md")
        # Because the frontmatter is missing/incomplete, the construction 
        # should fail.
        TaskFileBuffer(task_file_path)

def test_malformed_tasks():
    with pytest.raises(TaskFileException):
        task_file_path = get_test_file_path("invalid_2.md")
        TaskFileBuffer(task_file_path)

def test_improper_heading():
    with pytest.raises(TaskFileException):
        task_file_path = get_test_file_path("invalid_3.md")
        TaskFileBuffer(task_file_path)

def test_remove_up_to_date():
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    tasks = task_file_buffer.remove_tasks_up_to_date(datetime(year=2022, month=9, day=21))
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
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    tasks = task_file_buffer.remove_tasks_up_to_date(datetime(year=2022, month=9, day=30))
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
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    tasks = task_file_buffer.remove_tasks_up_to_date(datetime(year=2022, month=8, day=10))
    assert(tasks == [])

def test_append_tasks():
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

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
    task_file_buffer.insert_task_columns(new_tasks)

    assert(task_file_buffer.tasks == [
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
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    task_file_buffer.insert_task_columns([])
    assert(task_file_buffer.tasks == [
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
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    # Hit.
    index = task_file_buffer._search_for_task_date(0, 6, datetime(year=2022, month=9, day=21))
    assert(index == 2)

    # No hit.
    index = task_file_buffer._search_for_task_date(0, 6, datetime(year=2022, month=9, day=1))
    assert(index == 0)
    index = task_file_buffer._search_for_task_date(0, 6, datetime(year=2022, month=9, day=29))
    assert(index == 7)

def test_shift_incomplete_tasks_to_date():
    test_file_path = get_test_file_path("valid_1.md")
    task_file_buffer = TaskFileBuffer(test_file_path)

    date = datetime.strptime("2022-09-21", "%Y-%m-%d")
    task_file_buffer.shift_incomplete_tasks_to_date(date)

    assert(task_file_buffer.tasks == [
        (datetime(year=2022, month=9, day=19), [
            "- [x] [[_/(1 hour)  Set up git sync with mobile.]]"
        ]),
        (datetime(year=2022, month=9, day=20), []),
        (datetime(year=2022, month=9, day=21), [
            "- [ ] Go to CSESoc event.",
            "- [ ] **(1 hour)** Figma prototype.",
            "- [ ] ==2== 🏆 **Purpose today**: get chores done",
            "- [ ] ==2== **(2 hours)** Refine and review C++ notes #critical",
            "- [ ] ==1== Go to CPMSoc event.",
        ]),
        (datetime(year=2022, month=9, day=22), [
            "- [x] Install Linux VM on laptop, then VSCode with settings synced.",
        ]),
        (datetime(year=2022, month=9, day=23), []),
        (datetime(year=2022, month=9, day=24), []),
        (datetime(year=2022, month=9, day=25), [])
    ])

    date = datetime.strptime("2022-09-25", "%Y-%m-%d")
    task_file_buffer.shift_incomplete_tasks_to_date(date)
    assert(task_file_buffer.tasks == [
        (datetime(year=2022, month=9, day=19), [
            "- [x] [[_/(1 hour)  Set up git sync with mobile.]]"
        ]),
        (datetime(year=2022, month=9, day=20), []),
        (datetime(year=2022, month=9, day=21), []),
        (datetime(year=2022, month=9, day=22), [
            "- [x] Install Linux VM on laptop, then VSCode with settings synced.",
        ]),
        (datetime(year=2022, month=9, day=23), []),
        (datetime(year=2022, month=9, day=24), []),
        (datetime(year=2022, month=9, day=25), [
            "- [ ] ==4== Go to CSESoc event.",
            "- [ ] ==4== **(1 hour)** Figma prototype.",
            "- [ ] ==6== 🏆 **Purpose today**: get chores done",
            "- [ ] ==6== **(2 hours)** Refine and review C++ notes #critical",
            "- [ ] ==5== Go to CPMSoc event.",
        ])
    ])

def test_get_tasks_from_one_template():
    task_file_path = get_test_file_path("valid_1.md")
    template_file_path = get_test_file_path("valid_day_template_1.md", directory=TEMPLATE_FILE_DIRECTORY)
    task_file_buffer = TaskFileBuffer(task_file_path)

    assert(task_file_buffer._get_tasks_from_templates(template_file_path) == [
        "- [ ] Nuke Earth.",
        "- [ ] Invent a new virus."
    ])

def test_get_tasks_from_multiple_templates():
    task_file_path = get_test_file_path("valid_1.md")
    template_file_path_1 = get_test_file_path("valid_day_template_1.md", directory=TEMPLATE_FILE_DIRECTORY)
    template_file_path_2 = get_test_file_path("valid_day_template_2.md", directory=TEMPLATE_FILE_DIRECTORY)
    task_file_buffer = TaskFileBuffer(task_file_path)

    assert(task_file_buffer._get_tasks_from_templates(template_file_path_1, template_file_path_2) == [
        "- [ ] Nuke Earth.",
        "- [ ] Invent a new virus.",
        "- [ ] ### Save Earth.",
        "- [ ] Work on new indie game.",
        "- [ ] Learn a new song on guitar."
    ])

def test_cant_get_task_from_invalid_template():
    with pytest.raises(TemplateFileException):
        task_file_path = get_test_file_path("valid_1.md")
        template_file_path_1 = get_test_file_path("invalid_template_1.md", directory=TEMPLATE_FILE_DIRECTORY)
        template_file_path_2 = get_test_file_path("valid_day_template_1.md", directory=TEMPLATE_FILE_DIRECTORY)
        task_file_buffer = TaskFileBuffer(task_file_path)

        task_file_buffer._get_tasks_from_templates(template_file_path_1, template_file_path_2)
