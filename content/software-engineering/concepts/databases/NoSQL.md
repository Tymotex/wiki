---
title: NoSQL
description: NoSQL
---

TODO.

## Database Design
Best practices sourced from [official Firebase docs](https://firebase.google.com/docs/database/web/structure-data).
- **Don't nest too deeply**. When you fetch a part of the JSON, you also fetch all of its children. Permissions applied to the parent also apply to the children.
- **Flatten data structures**. Extract out nested sub-JSON structures so that they can fetched independently.
