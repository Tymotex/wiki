---
title: Database Index
---

A **database index** is a supplementary data structure that lets you quickly look up specific rows in a table.

They're usually a subset of the table being indexed.

Supposing you issued a `SELECT * FROM Table WHERE FirstName = "Linus"` query, without an index it would require a linear scan to get the result. To speed up these queries, you could 'create an index on the `FirstName` column', where you maintain a separate table containing the `FirstName` column that's sorted alphabetically. With this index, you can determine which row to find `FirstName = "Linus"` using binary search, then look it up in the original table.

The benefits and drawbacks are:
- Faster queries.
