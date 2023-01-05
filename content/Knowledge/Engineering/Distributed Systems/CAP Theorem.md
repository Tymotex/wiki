---
title: CAP Theorem
---

CAP theorem states that a distributed system can only have 2 of the following hold true:
1. Consistency — every node has the most recent data. I.e. if you pick any node, you will see all of them report the same data.
2. Availability — every request is fulfilled.
3. Partition tolerance — the system continues operating when some nodes can't communicate with each other.

