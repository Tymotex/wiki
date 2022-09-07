---
title: Pragmatic Programmer
---

### Being a Craftsman
> Care about your craft.

> Never run on auto-pilot. Constantly be thinking and critiquing your work in real time.

There is always opportunity to exercise your individual craftsmanship and individuality.

### Being a Student
> Every day, work to refine the skills you have and to add new tools to your repertoire.

> Your knowledge and experience are your most important day-to-day professional assets.

> Your ability to learn new things is your most important strategic asset.

#### Learning Goals
Sourced from the chapter, "Your Knowledge Portfolio".
- Learn a new language a year, at least. 
- Read at least one engineering book each month. Try to match the book's topic with something that will aid in the current project you're working on.
	> While there's a glut of short-form essays and occasionally reliable answers on the web, for deep understanding you need long-form books.
- Read at least one non-technical book each month.
- Attend social meetups and conferences.
- Constantly read about latest technology trends.
The purpose need not be to advance your career or enrich your resume. It should be to constantly push your ability to learn and think deeply.

### Being Pragmatic
Constantly consider the business value in your work.

### Being a Team Player
> Trust in a team is absolutely essential for creativity and collaboration according to the research literature.

> There's one technique that you must use if you want people to listen to you: *listen to them*.

> Unless you work in a vacuum, you need to be able to communicate. The more effective that communication, the more influential you become.

#### Stone Soup
When you're in a unique position with an idea but would struggle to marshal the team's focus and resources and approval to work towards it, simply start it by yourself. 
> People find it easier to join an ongoing success. Show them a glimpse of the future and you'll get them to rally around.

### Software Entropy
Software systems will always tend to accumulate software rot and technical debt. 

Do your absolute best to not leave bad designs and poor code unfixed. Have patience and fix each of them as they arise. Every time you allow 'broken windows' to stay unfixed, you let entropy win and start atrophying you and your team's morale. *[Hopelessness is contagious](https://pubmed.ncbi.nlm.nih.gov/7932064/)*
> Neglect accelerates software rot faster than any other factor.

> Just tell yourself, "No broken windows."

### ETC
Good designs are *easier to change* (*ETC*) than bad design. Generally, prefer to adopt an approach that is easier to change.

This implies that you should always prefer decoupled and cohesive modules over tight coupling.

### DRY
*Don't repeat yourself* is a classic acronym that means much more than just not copy and pasting your code and tweaking it slightly. The main concern is duplication of *knowledge*. When knowledge is duplicated, it is no longer a single source of truth and therefore can cause inconsistency.

> Some instances of code duplication are not violations of DRY. If tweaking one thing does not mean tweaking another, then those things are separate pieces of *knowledge*, generally.

### Orthogonality
Two parts of a software system are said to be *orthogonal* if changes in one do not affect the other. Always strive to make unrelated parts of a system orthogonal. Ie. decouple and isolate things as much as you can.

For example, the user interface should usually be orthogonal to the database schemas.

The primary purpose of [[Pragmatic Programmer#Refactoring|refactoring]] is to improve orthogonality between parts of the software and improve readability.

### Prototyping
Prototyping is a standard way to try out the feasibility of an idea and prove a concept without significant investment in time and resources. What you produce is meant to be discarded.
> Prototyping is a learning experience. Its value lies not in the code produced, but in the lessons learned. That's really the point of prototyping.

Things that are great candidates for prototyping are:
- System architecture. Draw out the main components and how they interact with each other on LucidChart.
- UI. Draw it on Figma or sketch something very low fideltiy on paper.
- Algorithms. Write it out in quick-to-write scripting language.

### Debugging
> Embrace the fact that debugging is **problem solving**, and attack it as such.

When fixing bugs, *always start by reproducing it*. Write a test that executes those steps and asserts the state to be what you expect in the bug-free version. Use a debugger to step through the code via the failing test.

- **Binary chopping**:
	Use a divide-and-conquer binary search approach to isolating where the problem might be. You'll converge on the problematic code very quickly.
- **Logging**:
	Also called *printf debugging*. This is primitive, but effective for simple bugs. It's still a good strategy for debugging problems where time is a factor such as concurrent programs.
- **Rubber ducking**:
	Explain the bug to someone else. It's effective because it forces you to explicitly state your assumptions and consequently begin to question them, which often leads to the bug source. A rubber duck is traditionally used. 

### Assertions


### Design by Contract


### Finite State Machines

### Observer Pattern

### Publish/Subscribe
Publish/subscribe (pubsub) is a generalisation of the observer pattern.

### Transforming
It's helpful to think of programming problems as data transformation problems. Consider what pipeline of transforms is necessary to get from the input to the expected output.

Some languages let you use a pipeline operator like `|>` to write something like
`"hello world" |> capitaliseTitle() |> print()`, which is equivalent to `print(capitaliseTitle("hello world"))`. The outcome is the same, but the pipelining approach is often a very different way of thinking that suits a lot of programming problems and leads to flatter and cleaner code.

The programming language doesn't need to support a pipelined operator for you to think and express code in this manner.

### Inheritance Tax
Inheritance couples a child to its parent and all its ancestors. Even worse, any object calling methods on the child is *also* coupled to its parent and all its ancestors. There's also the multiple inheritance problem... and the lack of support for it in languages like Java and the confusing semantics of it in C++.

Another problem is that when you inherit from a class, you are probably unnecessarily inheriting a bloated set of methods and properties. This does have some performance impacts, causing the object to take longer to initialise and more memory to store ([source](https://stackoverflow.com/questions/54362591/does-inheritance-can-affect-performances-of-an-application)).

In general, always prefer these 3 alternatives instead of inheritance.
1. Interfaces.
2. Delegation.
3. Mixins and traits.

### Managing Configuration
If your app needs some configuration values (like IP addresses, credentials, etc.) that might change after deployment to production, you should keep them behind an external service that serves them.

It should not be the case that you have to restart your application for changes to configuration to take effect, especially if your app must be highly available.

Consider *Configuration as a Service*.

## Refactoring

