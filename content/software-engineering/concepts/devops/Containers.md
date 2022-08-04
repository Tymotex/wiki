---
title: Containers
description: Containers
---

A *container* is a *process*, which runs in its own *isolated [[software-engineering/concepts/operating-systems/User Space & Kernel Space|user space]]*, that runs an app within. It contains everything required to run the app, which is basically the app's source code and all its dependencies.
- Running in an 'isolated' user space means that . Normally, if you spawn a process on your machine, it can see many things in its environment
- From each container's point of view, they have an entire operating system to themselves.

[Namespaces](https://en.wikipedia.org/wiki/Linux_namespaces) and [cgroups](https://en.wikipedia.org/wiki/Cgroups) (control groups) are what enable containers able to be run in an isolated user space and have their compute resources able to be monitored and restricted.

Containers are defined by a manifest file, which details everything necessary to get your app running within it. In [[software-engineering/technologies/Docker|Docker's]] case, that manifest file is the *Dockerfile*.

Containers are pretty much like [[software-engineering/concepts/devops/Virtual Machines|system virtual machines]], but they tend to use far fewer compute resources (like CPU, memory and disk space) and are quicker to spawn, making them great for on-demand [[software-engineering/concepts/cloud/Scaling|scaling]]. 


It's said that containers *virtualise* the operating system, 

*Containerisation* is the process of making apps run inside containers.

Multiple containers running on the same machine will share the same host operating system services and resources.



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

