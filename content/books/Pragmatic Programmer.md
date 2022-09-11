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

When you find a problem. Fix it right now.

### ETC
Good designs are *easier to change* (*ETC*) than bad design. Generally, prefer to adopt an approach that is easier to change. As a general (and oversimplified but still useful) rule, the quality of a design is measured by the ease with which you can make changes to that design.

This implies that you should always prefer decoupled and cohesive modules over tight coupling.

### DRY
*Don't repeat yourself* is a classic acronym that means much more than just not copy and pasting your code and tweaking it slightly. The main concern is duplication of *knowledge*. When knowledge is duplicated, it is no longer a single source of truth and therefore can cause inconsistency.

> Some instances of code duplication are not violations of DRY. If tweaking one thing does not mean tweaking another, then those things are separate pieces of *knowledge*, generally.

For example, two different CSS rules have `float: left;` doesn't necessarily count as a violation of DRY.

Blindly striving towards DRY can lead to forced abstractions and over-engineered code that's harder to maintain.

### Orthogonality
Two parts of a software system are said to be *orthogonal* if changes in one do not affect the other. Always strive to make unrelated parts of a system orthogonal. Ie. decouple and isolate things as much as you can.

For example, the user interface should usually be orthogonal to the database schemas.

The primary purpose of [[books/Pragmatic Programmer#Refactoring|refactoring]] is to improve orthogonality between parts of the software and improve readability.

### Tracer Bullets

![[tracer-bullet-development.png|550]]
([source](https://www.freecodecamp.org/news/lessons-learned-from-the-pragmatic-programmer-and-the-clean-coder/))

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
Refactoring is the 
> "disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behaviour." — Martin Fowler.

> Time pressure is often used as an excuse for not refactoring. But this excuse just doesn't hold up: *fail to refactor now, and there'll be a far greater time investment to fix the problem down the road*, when there are more dependencies to reckon with.

> Manage the pain: if it hurts now, it's going to hurt more later... Don't live with broken windows.

Always have a test suite to provide insurance that your refactoring efforts don't break the original design's correctness. In other words, have confidence you don't cause regression bugs.

## Testing
An underrated reason to write tests is because it forces you be a client of your code rather than a consumer.
> A test is the first user of your code.

When you're a client of the code, you're **forced to understand the specifications for the code you intend to write** rather than 'working it out as you go along'. It's a common mistake to start coding a function without a clear understanding of its inputs and outputs, and what the [happy path](https://en.wikipedia.org/wiki/Happy_path) is and what the error cases are.

> Making your stuff testable also reduces its coupling.

A fortunate consequence of writing unit tests is that it helps you decouple the thing you're testing from the rest of the system. For example, if you're testing a function that needs to talk with the database, then you would need to pass in a mock database interface from the unit test. This helps with decoupling that function because it might otherwise directly consume a global database handle.
```c++
void do_something() {
	global_db.get_thing();
}

void do_something(Database db) {
	db.get_thing();
}
```

> All software you write *will* be tested—if not by you and your team, then by the eventual users—so you might as well plan on testing it thoroughly.

> You really only have a few choices:
	- Test first (TDD)
	- Test during
	- Test never (which is what people mean when they say "test later")

Testing *is* programming. It's not something to be thrown over the wall to dedicated 'testers'.

### TDD
Being a TDD zealot and blindly following its steps rigorously all the time might seem like good practice, however it can lead you to endlessly polish the easy problems and build out features from the bottom-up rather than focusing on the end-to-end. Always remember the bigger picture of what you need to get done in the long term.

### Ad-Hoc Testing
Ad-hod testing is when you test the system in an improvisational way (by essentially just stumbling around observing for errors). It's a good way for generating more unit tests that you didn't think of.

### Property-Based Testing
TODO.

Property-based testing is about verifying invariants. It's complementary to your regular suite of unit tests.

## Security
1. Minimise attack surface area.
	- Never trust user inputted data. Always sanitise it before usage and storage.
	- Less code is easier to secure. Prefer less code.
2. Principle of Least Privilege. If a task requires a certain authorisation level, then grant the minimum set of permissions possible and revoke it as soon as possible.
1. Set secure default values. Let the user decide how they trade off convenience for security.
2. Encrypt sensitive data. Never store personally identifiable information in plaintext. In the event of a breach, the encrypted values are useless to the attacker.
3. Maintain security updates. When you need a security update, your system is vulnerable to a *known* exploit.

## Naming
Think *"what is my motivation for creating this?"*
```java
public void deductPercent(double amount);

// ... what is my motivation for creating this? Oh, it's to apply a discount.

public void applyDiscount(Percentage amount);
```

## Agile
The *Pragmatic Programmer* authors, Andy and Dave, were part of the group of software developers who got together to write the [Agile manifesto](https://agilemanifesto.org/) (another member of that group was Robert C. Martin, the author of *Clean Code*).  

> "Agile is not a noun"

Agile mandates nothing about what processes you follow. It's literally just a set of guiding values.
