---
title: Docker
description: Docker
---

Docker is a [[software-engineering/concepts/devops/Containers|containerisation]] tool, or *container runtime*, that packages up an app's source code and dependencies into portable containers that can be run in many different environments. Since a Docker container packages *all* the app's dependencies, just distributing the **Docker image** for that container is sufficient for anyone to run the app anywhere without needing to install anything else. There are alternative container runtimes like [Rocket](https://www.redhat.com/en/topics/containers/what-is-rkt) or [LXD](https://linuxcontainers.org/lxd/).

When you *Dockerise* an app, you get portability. That's the main reason people use it. This means you can have a lot of confidence that the app will work on anything that has a *Docker daemon* running on it, whether it's your laptop, your co-worker's laptop, a VM in a data center, a computer in your office, and so on (with some caveats like not being able to run Windows containers on Linux hosts). Docker is especially great for deploying [[software-engineering/concepts/architecture/Microservice|microservices-based]] applications.




## DockerHub
Many container runtime systems have a big public repo of container images. In Docker's case, we have DockerHub. There you'll find images for containers that run, for example, [PostgreSQL](https://hub.docker.com/_/postgres/), [NGINX](https://hub.docker.com/_/nginx), [Node.js](https://hub.docker.com/_/node), [Ubuntu](https://hub.docker.com/_/ubuntu/), etc.

## Containers vs. Virtual Machines
TODO.

Containers are considered substantially more lightweight than virtual machines.

Containers can have its own concept of a filesystem, networking resources, ...

Docker shares the host operating system's resources. 

## You can run an operating system in a container??
Most Docker examples you see will involve using a base container image containing a Linux distribution like the [official DockerHub image for Ubuntu](https://hub.docker.com/_/ubuntu/).

Docker containers do not contain a complete OS like a virtual machine, it just has a snapshot of the filesystem of a 'donor' OS. This idea is powerful enough that you can run a Linux distribution's entire application layer inside a container, eg. the package manager (`apt`, `pacman`, etc.), spawning a shell, etc.

Not every container 'has' an operating system. You won't be able to launch a shell in a container that doesn't have one.

## Under the hood
TODO.
