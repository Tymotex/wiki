
import os
import glob

import pytest

from journal_templater.journal_manager import JournalManager

TEST_JOURNAL_DIRECTORY = os.path.join(os.path.dirname(__file__), "journal-output")
TEST_JOURNAL_TEMPLATE_FILE_PATH = os.path.join(os.path.dirname(__file__), "journal-template.md")
TEST_JOURNAL_VARIABLES_FILE_PATH = os.path.join(os.path.dirname(__file__), "journal-variables.yml")

def clear_files_in_directory(path: str):
    files = glob.glob(os.path.join(path, "*"))
    for each_file in files:
        os.remove(each_file)

@pytest.fixture()
def journal_directory():
    clear_files_in_directory(TEST_JOURNAL_DIRECTORY)
    yield
    # clear_files_in_directory(TEST_JOURNAL_DIRECTORY)

class TestJournal:
    def test_journal_manager_instantiation(self, journal_directory):
        JournalManager(TEST_JOURNAL_DIRECTORY, TEST_JOURNAL_TEMPLATE_FILE_PATH, TEST_JOURNAL_VARIABLES_FILE_PATH)

    def test_journal_manager_file_creation(self, journal_directory):
        journal_manager = JournalManager(TEST_JOURNAL_DIRECTORY, TEST_JOURNAL_TEMPLATE_FILE_PATH, TEST_JOURNAL_VARIABLES_FILE_PATH)
        journal_manager.create_journal_entries(7)

        # We expect the journal directory to have 8 files, one for today's 
        # journal entry and then one for each of the next 7 days.
        assert(len(glob.glob(os.path.join(TEST_JOURNAL_DIRECTORY, "*.md"))) == 8)


