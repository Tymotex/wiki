---
title: Borg
---

A distributed 'cluster operating system' that handles computing resource allocation. To run something, Borg 
![[Knowledge/Engineering/SRE/assets/borg-architecture.png|500]]

Borg runs *jobs*, which are indefinitely running services or one-off things like a MapReduce. *Jobs* consist of 1 or more identical *tasks*. 

