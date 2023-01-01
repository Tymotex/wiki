---
title: Troubleshooting
---

> Always approach the problem with a rational and calm mind. It's tempting to make knee-jerk solutions that simply exacerbate the problem.

![[Knowledge/Engineering/SRE/assets/troubleshooting-flowchart.png|450]]
0. Know the *expected* state and the *actual* state.
1. **Triage** — figure out what's wrong. Always the first step.

This approach to troubleshooting mimics the scientific method:
1. Hypothesis — make a conjecture.
2. What are the consequences you expect from this hypothesis?
3. Seek or produce evidence that confirms or refutes the hypothesis.
4. If the hypothesis fails, propose a new one and repeat.

Beware of confusing correlation for causation.
> "Some correlated events, say packet loss within a cluster and failed hard drives in the cluster, share common causes — in this case, a power outage, though network failure clearly doesn't cause the hard drive failures nor vice versa. Even worse, as systems grow in size and complexity and as more metrics are monitored, it's inevitable that there will be events that happen to correlate well with other events, purely by coincidence." — Google SRE book.
