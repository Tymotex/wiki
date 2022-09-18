There will be 2 files:
1. Archive file 
2. File containing current and future dates' tasks.

**Requirements**:
Make this a CLI script. It should be able to run on system startup *and* it should be invokeable.
- All dates earlier than today should be moved to the archive file.
- All previous unchecked tasks from prior day should be moved to today.
- Column should show date in universal ISO format.
  Eg. "Monday (2022-09-17)"
- File for current and future dates should show up to 30 dates in the future.
- CLI option to append a number of new days to the task buffer.
    - Actually, it may better for it to automatically insert up to 30 dates in the future on startup.
