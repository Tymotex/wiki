

"""
1. Generate the journal files for up to num_future_dates.
    If YYYY-MM-DD already exists, skip.
    Else:
        Make that file
        Read in an interpolate the variables, pulling a random item from the
        pool of things in the yaml file.
        Commit, and repeat for num_future_dates.

Use re.sub to input in journal prompts and quotes.
Raise error: unrecognised journal item: '...'
Don't forget to document how this all works.
"""

class JournalManager:
    def __init__(self, journal_directory_path: str) -> None:
        self._journal_directory_path = journal_directory_path

        # Since we are working with direct date comparisons to universal ISO
        # dates of form YYYY-MM-DD, we must normalise the date today to be the
        # midnight time.
        self._date_today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    def create_journal_entries(self, num_future_dates: int) -> None:
        """
        Creates all journal entries spanning from today to the number of future
        dates from today.
        All journal entries are named following the format YYYY-MM-DD.md.
        If an entry already exists, it is not touched.
        """
        last_date = self._date_today + timedelta(days=num_future_dates)
        curr_date = self._date_today
        while curr_date <= last_date:
            pass
