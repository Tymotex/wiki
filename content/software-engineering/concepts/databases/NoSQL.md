---
title: NoSQL
description: NoSQL
---

> In this set of notes, we only consider *document-oriented* databases such as MongoDB and Firebase Realtime DB. There are also other types of NoSQL databases such as graph databases (like [Neo4j](https://neo4j.com/)) and simple key-value stores like [Redis](https://redis.io/) or [Memcached](https://memcached.org/).

*NoSQL* ("**n**ot **o**nly SQL") databases are those that ditch the idea of defining data using relational theory involving tables, rows and columns and linking them together.

**Why NoSQL over relational databases?**
The main two reasons are *flexibility* and *easier scaling*:
1. NoSQL uses flexible data models that are easier to modify in response to changes in business requirements or the query patterns of the users compared to relational databases.
2. Database servers are easier to scale horizontally through [[software-engineering/concepts/databases/Sharding|database sharding]]. It's challenging to shard relational databases.

## Data Modeling
Although non-relational databases don't have tables, rows and columns, and are often chosen in anticipation of changes to the data model, you still need to have a concrete idea of what the data model/schemas for your application look like. 

One good reason for this is because there is a [[software-engineering/concepts/databases/NoSQL#Don't Nest Deeply|tradeoff between data access speed and data redundancy]]. 


Things to think about:
1. Selecting a primary key.
2. What fields should be indexed.




Best practices (sourced from [official Firebase docs](https://firebase.google.com/docs/database/web/structure-data), [this article](https://proandroiddev.com/working-with-firestore-building-a-simple-database-model-79a5ce2692cb)).

### Don't Nest Deeply

- **Don't nest too deeply**. When you fetch a part of the JSON, you also fetch all of its children. In the case of managed databases like Firebase realtime db, the permissions applied to the parent also apply to the children.
    ```json
    ```
    
    
    To avoid nesting deeply, aim to **flatten** your data structures (also called *normalising*). Extract out nested sub-JSON structures so that they can fetched independently.

When you flatten data structures however, you increase *data redundancy* where the same data appears in multiple locations in the database.

TODO: when you have redundancy, how do you ensure changes are propagated??


When deciding whether to nest or not to nest, think about:
- 

- How often users will need to access a collection's documents. If the answer is *very frequently*, then optimise for data access speed at the cost of greater redundancy.