---
title: Building a Second Brain
---

## Tasks
- [ ] How do I stay on top of project deadlines? Idea: add a default card to each day that links to deadlines (maybe in the 'Purpose' card?).
- [ ] Complete my weekly review and monthly review templates.
- [ ] Write a Python script that generates a set of journal prompts.
- [ ] Make the task formatter increment a counter tag that shows how many times a task has been pushed along.

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
