---
title: Borg
---

A distributed 'cluster operating system' that handles computing resource allocation. If you want to run something, you tell Borg how many CPU cores and RAM you need, and it handles finding the machines in the cluster its overseeing to run it on. Borg also handles restarting things when they fail.

![[Knowledge/Engineering/SRE/assets/borg-architecture.png|500]]

Borg runs *jobs*, which are indefinitely running services or one-off things like a MapReduce. *Jobs* consist of 1 or more identical *tasks*.

## BNS
**BNS** (Borg Naming Service) is a level of indirection necessary for Borg to identify tasks (similar to DNS and IP addresses). It maps a unique string like `/bns/<cluster>/<user>/<job_name>/<task_number>` to an `<IP address>:<port>`.
