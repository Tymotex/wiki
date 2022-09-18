# Tasks Formatter
A CLI app that moves forward incomplete tasks from previous dates to the current
date and extends the current task list with the next 30 days. It's meant to be
used with `obsidian-kanban` but can be used without it.

This CLI works with two files (which will be created if they don't exist).
1. Archived tasks file named `archived-tasks.md`. This contains all the complete tasks and previous dates.
2. Current tasks file named `tasks.md`. This contains all the current and future tasks.

## Usage
```
tasks-formatter <path_to_tasks_directory>
```
This will modify/create `archived-tasks.md` and `tasks.md` in the given tasks
directory.

This script should also be run on system or app startup so that the tasks are
automatically formatted.

## Implementation Requirements
- All dates earlier than today's date should be moved to the archive file.
- All previous incomplete tasks from the prior day should be moved to today's 
  task buffer.
- Column should show the day of the week and the date (Eg. 19th Sep).
- The file for current and future dates should show up to 30 dates in the
  future. The number of future days should be tweakable with a CLI flag.

