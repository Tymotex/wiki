from datetime import datetime
from tasks_formatter.task_file_buffer import TaskFileBuffer

class TaskManager:
    def __init__(self, archived_task_file_path: str, task_file_path: str) -> None:
        self._archived_tasks_buffer = TaskFileBuffer(archived_task_file_path)
        self._tasks_buffer = TaskFileBuffer(task_file_path)
        self._date_today = datetime.now()

    def archive_past_task_dates(self):
        """
        Moves all the task columns for dates before today to the archived tasks
        file.
        """
        tasks_to_archive = self._tasks_buffer.remove_tasks_up_to_date(self._date_today)
        self._archived_tasks_buffer.insert_task_columns(tasks_to_archive)

    def shift_incomplete_tasks_to_today(self) -> None:
        """
        Moves all incomplete tasks before today to today's task column.
        """
        self._tasks_buffer.shift_incomplete_tasks_to_today() 
