---
title: Cypress
description: Cypress is an integration testing library for testing web apps.
---
Cypress is an [[software-engineering/concepts/testing/End To End Testing|end-to-end testing]] library for testing the entirety of a web app, including its frontend and backend, in a way that closely simulates how real users would use the app. It also has an API for writing [[software-engineering/concepts/testing/Integration Testing|integration tests]] and [[software-engineering/concepts/testing/Unit Testing|unit tests]]. 

Cypress tests aim to simulate the user experience as closely as possible. This means that tests you write will usually start up a real browser process, navigate to the URL of your web app, then execute a series of user interactions (eg. clicking on links, buttons, sending keystrokes, etc.) and let you make assertions on how the document should respond and what its contents should have.

The purpose of end-to-end testing this way is to give you confidence that the user can perform critical actions without error. For example, you might have a test that verifies your web app's authentication system, the purchase of an item, the sending of a message, etc. Unit tests with [[Jest]], for example, wouldn't be sufficient for that purpose.

### Writing Tests

TODO.

In general, the [[software-engineering/concepts/testing/Arrange, Act, Assert|arrange, act, assert]] pattern for writing unit tests is also a useful way to structure e2e Cypress tests.

**Note**: `describe` and `it` are sourced from [Mocha](https://mochajs.org/) and `expect` is sourced from [Chai](https://www.chaijs.com/), two core dependencies of Cypress.

### Cypress CLI
The Cypress package ships with a powerful CLI. [Official reference](https://docs.cypress.io/guides/guides/command-line).

Some basic commands to know and consider adding to the NPM scripts inside `package.json`:
```bash
cypress open                                       # Opens Cypress' Electron binary.
cypress run --headed --no-exit --browser chrome    # Opens a Chrome browser to run Cypress tests.
cypress run --browser chrome                       # Runs Cypress tests in a headless Chrome process.
```

### Running Cypress on a CI Server

TODO.
