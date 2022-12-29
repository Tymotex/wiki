---
title: Site Reliability Engineering
---

**Questions**:
- What exactly is reliability?
- 

SREs are software engineers whose focus is to create *reliable*, scalable software systems. *Reliability* formally means: "the probability that [a system] will perform a required function without failure under stated conditions for a stated period of time." 

Reliability is a function of:
- *Mean time to repair (MTTR)*: time taken to restore system health.
- *Mean time to failure (MTTF)*: time taken for system to fail.

The focuses of creating reliable systems are:
- Availability
- Latency
- Performance
- Efficiency
- Change management
- Monitoring
- Emergency response
- Capacity planning


Google loosely enforces a 50/50 split between development and operations work for SREs. Coding skills are still critical.

> "Reliability is the most fundamental feature of any product" — Ben Treynor Sloss.

> "SRE is what happens when you ask a software engineer to design an operations team." — Ben Treynor Sloss.

> "Software Engineering has this in common with having children: the labour before the birth is painful and difficult, but the labour after the birth is where you actually spend most of your effort."

Costs of running software after reaching production typically constitute 40-90%, meaning it's almost never the case that deployed software requires less attention from software engineers.

In the traditional development/operations split, the operations team size would scale linearly with service size. A primary focus of SRE is automating away the needs for a growing operations team. The SRE team size scales sublinearly with service size.

> "One could equivalently view SRE as a specific implementation of DevOps with some idiosyncratic extensions."

# Fundamentals
- [[Knowledge/Engineering/SRE/Error Budget|Error budget]]
- [[Knowledge/Engineering/SRE/Monitoring|Monitoring]]





