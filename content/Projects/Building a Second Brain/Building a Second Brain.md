---
title: Building a Second Brain
---

- Version control: Need to make the private content exist in a private repository.
- Want to go through each book in my reading list and at least write a few sentences for each, explaining the main takeaways.

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
- Automate the creation of new weekly task boards.
    - Could keep this rolling. Eg. could write a script that automatically pushes forward tasks from previous day to the current day. Automatically archive previous days. Have columns for the next 6 days after today. 

## Features
- Mobile Git synchronisation with [Termux](https://termux.dev/en/) and [Termux:Widget](https://wiki.termux.com/wiki/Termux:Widget).
    - [Inspired from this blog post](https://werzum.github.io/tech/2022/02/13/Obsidian-Mobile-Sync.html). I wrote a simple shell script that can be executed manually in one press through Termux:Widget. All the shell script does it run git commands to pull and then push whatever changes I make through Obsidian.
    - The Git syncing could be accomplished through [Tasker,](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm&hl=en_AU&gl=US) I believe.
