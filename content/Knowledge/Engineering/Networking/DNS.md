---
title: DNS
description: DNS
---

DNS (domain name system) is a distributed system that maps **domain names to IP addresses**, e.g. `timz.dev` to `76.76.21.21`. Think of it like a distributed database, actually.

The DNS system consists of a globally spanning network of **DNS servers**, also called **name servers**, each of which is responsible for handling the mappings belonging to their part of the **hierarchical namespace**. 
![[Knowledge/Engineering/Networking/assets/hierarchical-namespace.png|500]]
At each node, a DNS request can be forwarded to the appropriate child. The leaf nodes are the **authoritative name servers**, which actually store the domain name to IP address mappings. *In resolving a DNS request, you are simply traversing this tree on a path to a leaf to get your answer*.

Initially, all domain name to IP address mappings were stored in a single `hosts.txt` file managed by Stanford Research Institute. This centralised approach DNS system clearly wouldn't scale well, so now we have a distributed network of name servers instead.

Every machine connected to the internet has a unique IP address.

## DNS Resource Records
Authoritative name servers.

# Flashcards
- What is the hierarchical namespace?
    - It's a big tree consisting of domain levels. 
