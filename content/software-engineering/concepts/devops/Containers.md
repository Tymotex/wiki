---
title: Containers
description: Containers
---

TODO.

### Containers vs. Virtual Machines
TODO.

Containers are considered substantially more lightweight than virtual machines.

Containers can have its own concept of a filesystem, networking resources, ...

Docker shares the host operating system's resources. 

Deploying multiple VMs onto a single machine will involve creating complete guest OSs and libs for each. There is no sharing of them.

The containers running on the same machine will share the host OS's resources. Deploying more containers will not mean duplicating guest OSs. You will be able to deploy more containers on a machine than VMs.

Supposing you had 3 services to be deployed, you could either spin up 3 separate VMs, each with an entire OS contained within, or you could spin up 3 containers, each sharing the same host OS kernel services. Both ways would work, but opting for containers is a much more resource-efficient and quicker deployment strategy.
![[software-engineering/concepts/devops/assets/virtual-machine-vs-containers.png|600]]
*(Image sourced from Nick Janetakis.)*

