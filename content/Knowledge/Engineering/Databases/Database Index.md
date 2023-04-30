---
title: Database Index
---

A **database index** is a supplementary data structure that lets you quickly look up specific rows in a table. They usually contain a subset of the table being indexed.

Supposing you issued a `SELECT * FROM Table WHERE FirstName = "Linus"` query, without an index it would require a linear scan to get the result. To speed up these queries, you could 'create an index on the `FirstName` column', where you maintain a separate table containing the `FirstName` column that's sorted alphabetically. With this index, you can determine which row to find `FirstName = "Linus"` using binary search, then look it up in the original table.

The tradeoff is that you get faster queries at the cost of using increased storage space and worsened performance for mutation (`INSERT`, `UPDATE`, `DELETE`) operations because you'd also have to modify the index to keep it up to date.

You define database indexes using `CREATE INDEX` in [[Knowledge/Engineering/Languages/SQL|SQL]], e.g.
```sql
CREATE INDEX name_index ON Users (FirstName);
```
Once defined, the database engine will make sure to attempt an index lookup any time there's a query on `FirstName`.

## Composite Index
You can create database indexes on multiple columns.
