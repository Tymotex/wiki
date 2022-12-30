---
title: Google Infrastructure
---

# Data Centre
Google's data centres are equipped with their own proprietary power, cooling and hardware.

A campus consists of multiple data centres, a data centre houses clusters, which houses racks, which houses thousands of machines. **Campus → data centres → clusters → racks → machines.**.
![[Knowledge/Engineering/SRE/assets/google-data-centre-topology.png|500]]
([source](https://sre.google/sre-book/production-environment/))

Machines are hooked up to each other through Google's [Jupiter](https://cloud.google.com/blog/topics/systems/the-evolution-of-googles-jupiter-data-center-network) network system.

Resource allocation is handled by [[Knowledge/Engineering/SRE/Borg|Borg]].

# Storage
1. **D** is the low-level file server that runs on almost all machines.
2. **Colossus** is a *distributed cluster filesystem* that wraps around D. A distributed filesystem is one that is spread out across multiple machines but presents a single logical interface to the client. From the client's perspective, they wouldn't know they're interacting with a filesystem split across many machines.
    - Colossus is the backbone of Google Cloud services and apps like YouTube, Drive, Gmail, etc.
    - It's a successor of Google File System (GFS), which was something that inspired the development of Hadoop, an open-source distributed filesystem.
3. **Bigtable** is a NoSQL DBMS offered as a service.
4. **Spanner** is a SQL DBMS, also offered as a service. It's *globally-consistent*, meaning that you can have confidence that data accessed anywhere is always up to date.
![[Knowledge/Engineering/SRE/assets/google-storage-stack.png|400]]
([source](https://sre.google/sre-book/production-environment/))

# Utility
- Chubby — a distributed lock service with an API that mimics a filesystem. It's used to store some small pieces of data and is responsible for coordinating access to that data.
- Borgmon
