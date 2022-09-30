

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

from datetime import datetime, timedelta
import os
import re
from typing import List
import yaml

class JournalException(Exception):
    pass

class JournalManager:
    def __init__(self, journal_directory_path: str, journal_template_file_path: str, journal_variables_file_path: str) -> None:
        # Assumes that the journal directory path is absolute.
        if not os.path.exists(journal_directory_path):
            raise FileNotFoundError(f"Journal directory does not exist at path '{journal_directory_path}'")
        if not os.path.isdir(journal_directory_path):
            raise NotADirectoryError(f"Path '{journal_directory_path}' must be a directory.")
        self._journal_directory_path = journal_directory_path

        if not os.path.exists(journal_template_file_path):
            raise FileNotFoundError(f"Journal template file does not exist at path '{journal_template_file_path}'")
        self._journal_template_file_path = journal_template_file_path

        if not os.path.exists(journal_variables_file_path):
            raise FileNotFoundError(f"Journal variables YAML file does not exist at path '{journal_variables_file_path}'")
        # Validate the journal variables YAML file.
        with open(journal_variables_file_path, "r") as variables_file:
            self._journal_variables = yaml.safe_load(variables_file)
            if "prompts" not in self._journal_variables or not isinstance(self._journal_variables["prompts"], list):
                raise yaml.YAMLError("Expected a 'prompts' key and array of values in YAML variables file.")
            if "quote" not in self._journal_variables or not isinstance(self._journal_variables["quote"], list):
                raise yaml.YAMLError("Expected a 'quotes' key and array of values in YAML variables file.")

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
        template_lines: List[str] = self._get_template_lines()

        # Generate all journal entry files up to `num_future_dates` into the
        # future from the current date.
        last_date = self._date_today + timedelta(days=num_future_dates)
        curr_date = self._date_today
        one_day = timedelta(days=1)
        while curr_date <= last_date:
            journal_filename = f"{curr_date.strftime("%Y-%m-%d")}.md"
            journal_path = os.path.join(self._journal_directory_path, journal_filename)
            if not os.path.exists(journal_path):
                # In the new journal file, paste in the journal template's
                # contents but with the variables within interpolated.
                with open(journal_path, "w") as journal_file:
                    lines_to_write = self._interpolate_prompt_in_lines(template_lines)
                    journal_file.writelines(lines_to_write)
            curr_date += one_day

    def _get_template_lines(self) -> List[str]:
        """
        Reads the template file and returns all its lines.
        """
        with open(self._journal_template_file_path, "r") as template_file:
            return template_file.readlines()

    def _interpolate_prompt_in_lines(self, lines: List[str]) -> List[str]:
        """
        Interpolates the variables in each line of the given list of lines
        with values sourced from the prompts YAML file.
        Variables are denoted with double braces and an identifier,
        eg. {{prompt}}.
        Currently, the only known identifiers are `prompt` and `quote`.
        """
        lines = lines.copy()
        
        # Must match non-greedily to allow for multiple variables on the same
        # line.
        re.compile(r"{{(.*?)}}")
        for line in lines:
            # Extract all variables referenced. 
            variables = []

            # Pull a random value from the bank of prompts or quotes and 
            # populate that variable

            # Interpolate those variables in.
            # replace() or re.sub()
        return []

    def _get_variable_value(self, variable: str):
        if variable.lower() == "prompt":
            pass
        elif variable.lower() == "quote":
            pass
        else:
            raise JournalException(f"Unknown variable type '{variable}'")
