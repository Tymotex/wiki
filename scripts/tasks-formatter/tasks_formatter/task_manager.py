from datetime import datetime, timedelta
from tasks_formatter.task_file_buffer import TaskFileBuffer

class TaskManager:
    def __init__(self, archived_task_file_path: str, task_file_path: str) -> None:
        # The TaskManager maintains 2 task files, one for archived tasks, the
        # other for current tasks.
        self._archived_tasks_buffer = TaskFileBuffer(archived_task_file_path)
        self._tasks_buffer = TaskFileBuffer(task_file_path)

        # Since we are working with direct date comparisons to universal ISO
        # dates of form YYYY-MM-DD, we must normalise the date today to be the
        # midnight time.
        self._date_today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    def format(self, num_future_dates: int):
        """
        Shifts all incomplete tasks to today and archives task columns before
        today's date.
        """
        self._shift_incomplete_tasks_to_today()
        self._archive_past_task_dates()
        
        last_column_date = self._date_today + timedelta(days=num_future_dates)
        self._tasks_buffer.add_columns_up_to_date(last_column_date)

    def _archive_past_task_dates(self):
        """
        Moves all the task columns for dates before today to the archived tasks
        file.
        """
        tasks_to_archive = self._tasks_buffer.remove_tasks_up_to_date(self._date_today)
        self._archived_tasks_buffer.insert_task_columns(tasks_to_archive)

    def _shift_incomplete_tasks_to_today(self) -> None:
        """
        Moves all incomplete tasks before today to today's task column.
        """
        self._tasks_buffer.shift_incomplete_tasks_to_date(self._date_today) 
