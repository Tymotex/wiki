---
title: Firebase
description: Firebase
---

![[software-engineering/technologies/assets/firebase-wallpaper.webp|750]]
Firebase is a set of services that help you start and scale your apps. It consists of an array of products such as:
- [Firebase Auth](https://firebase.google.com/products/auth) for setting up end-to-end user authentication without writing and maintaining the backend for it yourself.
- [Firebase DB](https://firebase.google.com/products/realtime-database), a realtime database (described as a giant JSON tree that bidirectionally communicates with clients, meaning updates can be pushed to connected clients).
- [Cloud Firestore](https://firebase.google.com/docs/firestore), a NoSQL database.
- Firebase Hosting for deploying web apps and static content to a CDN.
- [Cloud Functions](https://firebase.google.com/docs/functions) for running backend code in response to events without having to maintain your own servers or cloud VMs.
- [Firebase Remote Config](https://firebase.google.com/docs/remote-config).
... and a few more. They all have 'client-first' SDKs for JavaScript, Android, iOS, Flutter, Unity, etc. which means you can directly interact with Firebase products from your frontend without a backend.

tl;dr setup for the web:
```javascript
// 1. Create a Firebase project, then register your web app. 
//    at console.firebase.google.com.

// 2. In your project, get the JavaScript Firebase SDK
yarn add firebase

// 3. In your project, initialise firebase

    import { initializeApp } from "firebase/app";
    import { getAuth } from "firebase/auth";
    import { getDatabase } from "firebase/database";
    
    const firebaseConfig = {
      apiKey: "...",
      authDomain: "<project_id>.firebaseapp.com",
      projectId: "<project_id>",
      databaseURL: "https://<db_name>.firebaseio.com",
      ...
    };
    
    const app = initializeApp(firebaseConfig);
    const db = getDatabase(app);
    const auth = getAuth(app);
```

## Firebase Auth

## Firebase Realtime Database
Firebase DB is a [[software-engineering/concepts/databases/NoSQL|NoSQL]] *realtime* database, credited with low latencies. Being a 'realtime' database just means that any updates from one client can be pushed to subscribed clients within milliseconds. Firebase DB is a great choice compared to 'normal' databases like Cloud Firestore or PostgreSQL if you have a simple data model, small amount of data, and expect low-latency access. For more heavyweight use cases, pick Cloud Firestore.

All data is stored as JSON, in fact a Firebase DB instance is described as just ["a cloud-hosted JSON tree"](https://firebase.google.com/docs/database/web/structure-data). It looks like this, for example:
```json
{
  "users": {
    "alovelace": {
      "name": "Ada Lovelace",
      "contacts": { "ghopper": true },
    },
    "ghopper": { ... },
    "eclarke": { ... }
  }
}
```

When users lose network connection, the changes they'd otherwise push to the database are persisted locally in a cache, and then when they reconnect, those changes are automatically merged with the database.
