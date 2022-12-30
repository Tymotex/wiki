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


