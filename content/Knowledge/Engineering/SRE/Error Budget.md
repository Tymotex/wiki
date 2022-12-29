---
title: Error Budget
---

There is a fundamental tension between development and operations: the pace of innovation vs. the reliability of the software. 

In SRE, we use *error budgets* to resolve this tension. It is accepted that 100% reliability is not the correct target (unless you're building medical software or dangerous machinery), affording a small amount of unreliability in the system to allow for reasonable development velocity.

There is rarely any serious difference between software that works as promised 100% of the time versus 99.999% of the time. If we pick 99.999% as the reliability target, that affords us 0.001% as the error budget. This can be freely spent as long.
