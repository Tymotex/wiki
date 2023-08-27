---
title: Designing Data Intensive Applications
---

CPU clock speed improvements have saturated. Unless they can continue to improve at a rate that matches our demand on fast CPUs, there is no choice but to use *parallelism*.

*Data-intensive applications* refer to software where the main challenge is dealing with the massive amount of data and its complexity. *Compute-intensive* applications are those where CPU power is the main bottleneck rather than the amount/complexity of data.

## Chapter 1
- **Reliability**: fault-tolerance, or the "continuing to work correctly even when things go wrong."
	- It's not a bad idea to deliberately cause faults to continually exercise the system's reliability. E.g. you might constantly randomly kill servers, which is what [Netflix's Chaos Monkey](https://netflix.github.io/chaosmonkey/) does.
	- *Redundancy* is the first strategy to having fault-tolerance - when one thing dies, fail over to the backup.
- **Scalability**: when data/traffic/complexity grows, the system should toelrate that growth.
- **Maintainability**: how easy is this system to change.

There are a few universal things data-intensive software always need to do:****
- **Databases** - store stuff persistently.
- **Caches** - keep results of operations that were expensive to run.
- **Search indexes** - search through data quickly by using a supporting data structure called a search index.
- **Message queuing** - to communicate data between servers asynchronously.
- **Batch processing** - do computationally heavy things outside of the main serving logic.
![[Reading/assets/ddia-simple-data-system.png|600]]

Human errors in some systems are the *leading* cause of outages. Systems need to be designed in a way that account for the unreliability of human operators.
- Provide 'dev'/sandbox instances of the service so that human operators can test changes before committing those changes to production.
- Have fast and easy rollback mechanisms.
- Canarying - roll out new code changes slowly in a step-wise fashion.

**Fan-out** (and fan-in) is a challenge in some systems - where to serve one request you might need to do an operation that touches many different things in parallel. *A single request might expand into many operations*.
- E.g. you make a post to Facebook, then that needs to appear in the home feed of all your friends.
	![[Reading/assets/twitter-fan-out.png|700]]
	 - In Twitter's case, they need to care about a parameter called *fan-out load*, where one tweet request by Elon Musk might need to be distributed to 100 million+ followers.
- *Fan-out* - a term in electronic engineering describing the number of logic gates that a particular logic gate outputs to
	![[Reading/assets/fan-out.png|200]]


Questions:
- Telemetry vs. monitoring vs. observability.

Random notes:
- Monitoring:
	- Latency != response time. Response time is the metric specific to the experience of the user of your system. It's a time that includes all the delays along the way like network delays.
	- In monitoring, percentiles are generally much more useful than averages. The median (50th percentile value) is generally better at reflecting typical user experience.
	- Higher percentiles are referred to as 'tails'. In particular, tail latencies are of interest in many systems - e.g. in Amazon, the users experiencing tail latencies are often the most profit-producing customers.
		- *Tail latency amplification* is a common consequence arising from *head-of-line blocking*. If you send a request that is slow to process, it might 'clog the line' and your subsequent requests will also probably be slower.
- System design:
	- A discussion of 'scalability' should be in terms of 'how does this system cope with increases in X *load parameter*', where load parameters include things like: *fan-out load*, read-to-write ratio, etc.
	- The 'right' architecture for a service always depends on what the service expects its *load parameters* to be.
	- System designs should always strive to optimise for:
		- Operability: easy for ops teams to manage.
			- There should be good monitoring, good troubleshooting guides, good way to anticipate problems, etc.
		- Simplicity: easy for engineers to understand.
		- Evolvability: easy for engineers to make changes to.
  
## Chapter 2
Data modeling is deciding what interface/abstraction to present to the world, and what 'things' your system reasons with. The abstraction you presents matters a lot -- it defines what the systems using your service can and can't do.

**Relational data modeling** where you organise things into rows in tables, and have rows referencing rows in other tables, is the dominant way of data modeling for the few decades following its rise in 1970. Doing it this way tended to create very clean abstractions.

'NoSQL' was meant to just be a Twitter hashtag, but it became the main label we give to non-relational databases. It's been retroactively interpreted as 'not only SQL'.
- NoSQL databases were intended to be an answer to relational databases' scalability challenges for huge write traffic and huge tables, and as an alternative for expressing data models in a way that was more permissive and easy to evolve over time.
- **Object-relational mismatch problem** - if you model your system with OOP but use a relational database, then there needs to exist a way to map your system's object models to your relational database's table schema. *This is what an ORM (object-relational mapper) achieves*.

[Polyglot persistence](https://en.wikipedia.org/wiki/Polyglot_persistence) is the practice of using different kinds of data storage technologies for a service. It's a bit like polyglot programming where you use 2+ languages for one program in order to leverage the strengths of one language for specific requirements of the program.

In many cases, storing data as a JSON offers better **locality** than storing one part in a table and its many other related rows in a different table. To fetch certain data, you need only fetch the JSON and pull out the things you need, whereas you might need to write a somewhat complex SQL query touching multiple tables to get what you need.
- E.g. Consider your app that has users and posts. Users have many posts. Using a relational database, you'd have a `Users` table and a `Posts` table, where posts reference a `user_id`. In this case, getting a user and their posts together involves a SQL `SELECT ... FROM Users JOIN Posts ON Users.id=Posts.user_id`, for example. If you were to store a JSON, you could do it like this and just have one simple fetch for all the information you need:
```
{
	"users" = {
		"Linus": {
			...
			posts: [ ... ]
		},
		...
	}
}
```

**ID or raw string?** Often when designing the data model, you have a choice of making a string field an ID (which might come from a dropdown of fixed options) or a raw string which (might come from a freeform input field that the user types in).
- Reasons for using IDs:
    - It never needs to change because it has no human-readable meaning.
    - It reduces duplication, reduces risk of inconsistency between redundant copies, and makes updates have less overhead. Generally, this is the main idea behind **normalisation** in databases.
- Reasons *not* to use IDs:
    - Unlike relational databases, document-oriented databases may not support joins on IDs or have weak support for them. In that case, you'd have to do multiple queries... '*the work of making the join is shifted from the database to the application code.*'
    - 
