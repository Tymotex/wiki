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
2. **Colossus** is a *distributed cluster filesystem* that wraps around D. A distributed filesystem is one 
    - 
![[Knowledge/Engineering/SRE/assets/google-storage-stack.png|400]]
([source](https://sre.google/sre-book/production-environment/))

# Flashcards
- What are the 5 technologies constituting Google's storage stack?
    - They're D, Colossus, Bigtable, Spanner and Blobstore. D sits at the lowest level as a fileserver on almost every machine in a datacentre. Colossus wraps around D to create a distributed cluster filesystem.
