---
title: DNS
description: DNS
---

DNS (domain name system) is a [[Knowledge/Engineering/Architecture/Distributed System|distributed system]] that maps **domain names to [[Knowledge/Engineering/Networking/IP Addresses|IP addresses]]**, e.g. a DNS query for `timz.dev` can resolve to `76.76.21.21`. Think of DNS as a distributed database, actually. The whole point of the DNS system is to allow for you to talk to computers through human-readable domain names. That extra layer of indirection also allows for more security and for changing the underlying machine without affecting users (`timz.dev` could be migrated to a different host).

The DNS system consists of a globally spanning network of **DNS servers**, also called **name servers**, each of which is responsible for handling the mappings belonging to their part of the **hierarchical namespace**. 
![[Knowledge/Engineering/Networking/assets/hierarchical-namespace.png|500]]
At each non-leaf node, a DNS request can be forwarded to the appropriate child. The leaf nodes are the **authoritative name servers**, which actually store the domain name to IP address mappings. *In resolving a DNS request, you are simply traversing this tree on a path to a leaf to get your answer*.

Initially, all domain name to IP address mappings were stored in a single `hosts.txt` file managed by Stanford Research Institute. This centralised approach DNS system clearly wouldn't scale well, so now we have a distributed network of name servers instead.

## DNS Resource Records
Resource records.

Authoritative name servers hold the resource records for each domain name it manages.

## DNS Resolution
Suppose you want to visit `timz.dev`.
1. You start a Chrome web browser process and search for `timz.dev`.
2. Chrome asks the local DNS resolver for the IP address of `timz.dev`.
3. If the mapping doesn't exist in the cache, the DNS resolver forwards the request to the root DNS server.


# Flashcards
- What is the hierarchical namespace?
    - It's a big tree consisting of domain levels. At each non-leaf node, the DNS query is forwarded down until it gets to a leaf node, i.e. an authoritative nameserver, that actually holds the domain name to IP address mapping.
