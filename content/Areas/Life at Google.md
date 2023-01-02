---
title: Google Tasks and Workflow
---

## First Few Days
[[Knowledge/Soft Skills/Excelling as a Graduate|Excelling as a new software engineering graduate]].

Some questions to ask:
- Based on your personal experience, do you have any advice on *when* to ask for help?
- What do you consider are the strongest signals that an L3 is ready to transition to an L4 engineer?
- How different do you feel now compared to when you first started out? (Maybe be more specific here)
- Do you have any advice to would give to yourself when you were just starting out your career in software engineering?
- Is there anything you're learning about recently?
- Do you have any thoughts on how to best absorb all the information in the first few weeks?
- Do we like to do daily or weekly standups in this team?
- What are the consequences of not meeting SLA for Storage services? I'm curious because they're not user-facing.
- How often do disastrous outages actually happen for Storage services?
- What's been the most disastrous outage you've experienced?
- Can you think of any unique challenges faced by Storage SRE that aren't faced by any other SRE team?
- Are there ever intentional outages caused on the Storage services like there are for services like Chubby?
- Can I stay behind in the office after work to read or work on my own personal projects.
- How often is the work that the team does considered toil?
- Do people usually have two sets of peripherals, one for home, one for work? E.g. one keyboard they buy is left at work while one keyboard is left at home?
- How likely is it for something disastrous to happen to a Storage service without the monitoring services being able to pick up anything?
- How reliable are the monitoring services? What if they experience an outage — who's watching the watchers?
- How reliable are the tools or services you use to apply a fix in an incident? What if they break? E.g. what if the rollback mechanism does not behave correctly?
- How are the reliability targets determined for low-level services like for Storage? (it must be different to how they're determined for user-facing services like Gmail)
- How elaborate is the process of determining the reliability target and SLOs for a service? Do they change after being set?
- If Google's largest datacentre got nuked, would most of the services still be alive?
- What are the events that contribute to the error rate?
- How hard does monitoring impact a service's performance?
- What exactly does 'turnup' mean? I can't find a precise definition for it.
- When we talk about 'clusters', do we mean an arbitrarily sized group of machines, or do we mean a physical cluster in a data centre — exactly one group of racks?
- Do the people in this team generally work independently on their own projects, or do they frequently collaborate on the same project?
- Are SREs able to be swapped into the development team without much ramp up time?
- How do you plan your workdays? Do you know of any strategies that work really well for you?
- Do you have any programming book recommendations? 
- Does every SRE rely on a playbook? Do you find it useful in your experience or are most problems novel?
- What happens when both primary and secondary on-callers fail to mitigate a problem? Is the problem simply left to persist until the next workday?
- Roughly what fraction of pages are from the monitoring system versus from human escalation?
- If I wanted to deploy a simple web server to Google Cloud, does that web server end up as a job on Borg? If so, does that mean customers' jobs and internal jobs are all using the same set of physical computers?
- What are the differences between Borgmon and Prometheus?
- How common is it for an incident to fall through to the secondary on-caller.
- Do SREs work on feature development often? Or is their development work mainly done to improve the reliability of the service?
- How can I see past postmortems from this team?
- Are past outages tracked by this team using Outalator? May I see them?
- Are the metrics like MTTF and MTTR known for our services?
- What's the logic behind automated rollback? How do I know under which conditions this can happen?
    - Do SREs ever have to worry about the security of services? It seems like one thing that threatens reliability. Are our services safe from DDoS attacks (or does the impact of that get reduced by some protective layers)?

### First Tasks

- [ ] Questions to learn the answer to and maybe write about:
    - [ ] How does Blaze exactly work? What language is it implemented in?
    - [ ] What is Rapid's relationship to Blaze? Does it invoke Blaze?
    - [ ] Who writes the Codelabs?
    - [ ] I'm confused about what MPM is and how it fits into the release pipeline. Is it at all similar to npm?
- [ ] Codelab goals! Work on codelabs for \_ hours.

## Ideas
- From the first days, begin writing ELI5 resources for Nooglers and people new to SRE.
- Contribute a few source code documentation CLs to begin with.

## Workflow Checklist
- Use a tiled window manager such as i3.
    - Have the same shortcuts as the ones you use on your main PC.
- Set up the same Chrome extensions and keybindings as at home.
- Set up the same Obsidian setup (with permission, obviously).
    - Ideally: set up Quartz and host your knowledgebase. Wouldn't that be impressive?
    - Set up the kanban board.
    - Set up the daily notes and the template you'll use to log your accomplishments each day.

**Notes**:
- You **must** document your and achievements well. Do this in Obsidian as well. You'll need this for performance reviews and getting future roles. This might be the highest reward:effort ratio things you can do, and all these documented achievements will serve you for the entirety of your career.
    - Inspired from the channel 'A Life Engineered'. He suggest calling this a 'brag document' and adding new entries on-demand rather than on some daily/weekly basis.

## Things to do after work
- Take parents out to dinner.
- Walk along Darling Harbour bridge.
- Meet friends to chill.
- Study or read a book in a cafe.
- Attend some skills class in the city.
