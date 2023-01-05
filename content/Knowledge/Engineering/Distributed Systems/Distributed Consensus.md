---
title: Distributed Consensus
---

*Consensus* is the process of getting groups of processes to agree on something. The point of it is to ensure data *consistency* in a distributed system — i.e. if a node sees a value as X, then all other nodes should also see it as X. In financial systems for example, this is critical.

Distributed consensus algorithms help distributed systems achieve consistency.

## Paxos [TODO]
The Paxos algorithm, first described by Leslie Lamport, is used to get a distributed system's nodes to agree on one value.

- There are proposers, acceptors and learners.
    - Nodes can take multiple roles.
- All nodes are willing to 'change their mind' and agree to any value, provided that the majority agrees on it.
- 

It's basically democracy — the majority of nodes have to agree on a value.
