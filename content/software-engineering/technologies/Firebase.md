---
title: Firebase
description: Firebase
---

![[software-engineering/technologies/assets/firebase-wallpaper.webp|750]]
Firebase is a [[software-engineering/concepts/cloud/BaaS|BaaS]] platform which gives you set of services that help you start and scale your apps. It consists of an array of products such as:
- [Firebase Auth](https://firebase.google.com/products/auth) for setting up end-to-end user authentication without writing and maintaining the backend for it yourself.
- [Firebase DB](https://firebase.google.com/products/realtime-database), a realtime database (described as a giant JSON tree that bidirectionally communicates with clients, meaning updates can be pushed to connected clients).
- [Cloud Firestore](https://firebase.google.com/docs/firestore), a NoSQL database.
- [Firebase Hosting](https://firebase.google.com/docs/hosting) for deploying web apps and static content to a CDN.
- [Cloud Storage](https://firebase.google.com/docs/storage) for storing files/blobs.
- [Cloud Functions](https://firebase.google.com/docs/functions) for running backend code in response to events without having to maintain your own servers or cloud VMs.
- [Firebase Remote Config](https://firebase.google.com/docs/remote-config).
... and a few more. They all have 'client-first' SDKs for JavaScript, Android, iOS, Flutter, Unity, etc. which means you can directly interact with Firebase products from your frontend without a backend.

The main concern of adopting Firebase is [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in). Don't worry too much about it though.

#### Web Quick Setup
```javascript
// 1. Create a Firebase project, then register your web app at:
//    console.firebase.google.com.

// 2. In your project, get the JavaScript Firebase SDK
yarn add firebase

// 3. In your project, initialise firebase and the services you
//    intend to use. Grab all credentials from the Firebase console.

    import { initializeApp } from "firebase/app";
    import { getAuth } from "firebase/auth";
    import { getDatabase } from "firebase/database"; 
    // ... import more Firebase product SDKs as required.
    
    const firebaseConfig = {
      apiKey: "...",
      authDomain: "<project_id>.firebaseapp.com",
      projectId: "<project_id>",
      databaseURL: "https://<db_name>.firebaseio.com",
      ...
    };

    // Initialising Firebase and the services you intend to use.
    const app = initializeApp(firebaseConfig);
    const db = getDatabase(app);
    const auth = getAuth(app);
```

## Firebase Auth

### Snippets
Some code snippets to demonstrate Google sign-in, sign-out and grabbing Google profile information (sourced from the [official Codelab](https://firebase.google.com/codelabs/firebase-web)):
```javascript
import {                 // Firebase SDK auth functions.
    getAuth,
    onAuthStateChanged,
    GoogleAuthProvider,
    signInWithPopup,
    signOut,
} from 'firebase/auth';

// Signing in and out.
const signIn = async () => {
    var provider = new GoogleAuthProvider();
    await signInWithPopup(getAuth(), provider);
}
const signOutUser = () => signOut(getAuth())
const isUserSignedIn = () => !!getAuth().currentUser;

// Adding an event listener to when the auth state changes (ie. when the user
// signs in and out). This can be used to affect the UI, like the top nav.
const initFirebaseAuth = () => onAuthStateChanged(getAuth(), (user) => {
    if (user) ...
    else ...
});

// Retrieving things accessible in the user's Google profile like their name and display picture.
const getProfilePicUrl = () => getAuth().currentUser.photoURL || '/images/profile_placeholder.png';
const getUserName = () => getAuth().currentUser.displayName;
```

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

## Cloud Firestore
Cloud Firestore is a [[software-engineering/concepts/databases/NoSQL|NoSQL]] database

## Firebase CLI
The Firebase CLI is for deploying and managing projects from the terminal.
```bash
# Setup:
yarn global add firebase-tools
firebase --version
```

Some useful commands:
```bash
firebase init    # Creates `firebase.json` in the current directory and proceeds with
                 # a guided setup of your services.
firebase use     # View project aliases.
firebase serve   # Locally host the project so you can test it out before deploying to production.
```

