---
title: Building a Second Brain
---

- Go through each book in my reading list and at least write a few sentences for each, explaining the main takeaways.

## Automation Ideas
- Automate the initialisation of a new project with a Python/Rust/Go/Ruby script.
	- Use Tiago's preflight checklist:
		- Reminder: projects should always have an MVP definition, starting time and deadline. They're a big investment of time and energy and should be clearly aligned with your values.
		- What do you want to learn?
		- What challenges can you foresee?
		- What (further) research needs to be done?
		- What is the MVP? (For non-output based products, what is the success criteria?)
		- What are the stretch goals?
	- Use Tiago's postmortem checklist:
		- What did you learn?
		- What did you do well?
		- What could you have done better?

## Features
- Mobile Git synchronisation with [Termux](https://termux.dev/en/) and [Termux:Widget](https://wiki.termux.com/wiki/Termux:Widget).
    - [Inspired from this blog post](https://werzum.github.io/tech/2022/02/13/Obsidian-Mobile-Sync.html). I wrote a simple shell script that can be executed manually in one press through Termux:Widget. All the shell script does it run git commands to pull and then push whatever changes I make through Obsidian.
    - The Git syncing could be accomplished through [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm&hl=en_AU&gl=US) as well, I believe.
    - Using a service managed by `systemctl` which automatically runs a git commands to sync to remote on system shutdown.
- Python CLI that formats the task board when Obsidian starts up. It can also be invoked with a custom hotkey, `ctrl + alt + f`, made possible by `obsidian-shellcommands`.
    - Moves all incomplete tasks from previous days into today's task lane. This eliminates you having to manually drag cards over to today.
    - Creates the next $n$ days' task lanes and populates them with default tasks. For example, you can schedule a morning routine task for every day or a weekly review task for every Sunday, etc.
    - You only ever have to view and manage 1 task board. The script helps to keep the task board cycling onwards through the days infinitely.

## Workflow
- Vim keybindings option in Obsidian and `obsidian-vimrc-support`.
- `obsidian-kanban`  -> for managing daily tasks.
    - TODO: elaborate.
- `obsidian-dictionary` -> allows me to quickly look up the definition of a highlighted word via the context menu (which I bring up with `ctrl + r`).

## Shortcuts
I aimed to set keybindings that closely match how I have it in other programs like browsers, code editors and Vim.
- VSCode-like shortcuts:
    - `ctrl + ,` — bring up settings.
    - `ctrl + shift + b` — toggle left sidebar.
    - `ctrl + shift + e` — open file explorer.
    - `ctrl + shift + f` — broad search.
    - `ctrl + p` — search and open file by name.
    - `ctrl + shift + p` — open command palette.
- Notion-like shortcuts:
    - `ctrl + \`  — toggle right sidebar.
    - `ctrl + shift + l` — toggles light/dark theme.
        - *Note*: Obsidian doesn't support toggling, so the workaround is to use `ctrl + shift + alt +l` for light mode.
- Browser-like shortcuts:
    - `ctrl + w` — close the current window.
    - `ctrl + shift + t` — reopen the closed file.
- Vim-like shortcuts:
    - `alt + h/l` — navigate to previous/next file.
    - `ctrl + h/l` — focus on the left/right pane.
- `ctrl + r` — bring up context menu.
- `ctrl + j` — open daily note ('j' for 'journal').
- `ctrl + alt + f` — runs my custom Python CLI which formats my tasks.
