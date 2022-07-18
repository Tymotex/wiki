---
title: Cypress
description: Cypress is an integration testing library for testing web apps.
---
Cypress is an [[software-engineering/concepts/testing/End To End Testing|end-to-end testing]] library for testing the entirety of a web app, including its frontend and backend, in a way that closely simulates how real users would use the app. It also has an API for writing [[software-engineering/concepts/testing/Integration Testing|integration tests]] and [[software-engineering/concepts/testing/Unit Testing|unit tests]]. 

Cypress tests aim to simulate the user experience as closely as possible. This means that tests you write will usually start up a real browser process, navigate to the URL of your web app, then execute a series of user interactions (eg. clicking on links, buttons, sending keystrokes, etc.) and let you make assertions on how the document should respond and what its contents should have.

The purpose of end-to-end testing this way is to give you confidence that the user can perform critical actions without error. For example, you might have a test that verifies your web app's authentication system, the purchase of an item, the sending of a message, etc. Unit tests with [[software-engineering/frameworks/Jest]], for example, wouldn't be sufficient for that purpose.

### Writing Tests
In general, the [[software-engineering/concepts/testing/Arrange, Act, Assert|arrange, act, assert]] pattern for writing unit tests is also a useful way to structure e2e Cypress tests.

#### Example
A simple test suite I wrote for my portfolio website.
```typescript
describe("Portfolio page tests", () => {
    beforeEach(() => {
        // A wait exists just to allow for page-load animations to complete.
        cy.visit("/").wait(1000);
    });

    it("should render the about page after the 'about' link is clicked", () => {
        // Click 'About' from the homepage.
        cy.contains("About").click().wait(1000);

        // The window should show and the URL should change.
        cy.url().should("include", "/about");
        cy.contains("Who am I?");
    });

    // ...
});
```
**Note**: `describe` and `it` are sourced from [Mocha](https://mochajs.org/) and `expect` is sourced from [Chai](https://www.chaijs.com/), two core dependencies of Cypress.

### API
See [Cypress API Documentation](https://docs.cypress.io/api/table-of-contents). You'll be frequently chaining many methods together in a single statement.
- Methods like `cy.get` return a DOM element that can be further chained with methods like `type`, `click`, `contains`, etc.
- Some methods like `cy.clearCookies` do not yield anything that you can chain further methods on.

**Top-Level Methods**
```typescript
cy.visit(url)
cy.get(cssSelector)         // This works just like jQuery's `$()` selector. In fact, jQuery is one of Cypress' dependencies.
cy.url()                    // Gets the current URL as a string.
cy.wait(milliseconds)
```
**Note**: all of these `cy.*` statements execute asynchronously.

**Chained Methods**:
```typescript
.then((elem) => ...)        // You can access the 'subject' inside `then`. You'd chain this with `cy.get`, for example.
.should(chainer: string)    // Make an assertion. 
.and(chainer: string)       // An alias for `should`.

// Input methods:
.type(text: string)
.submit()
.click()
```
The `chainer` argument is a stringified *chainer* from [Chai](https://docs.cypress.io/guides/references/assertions#Chai), [Chai-jQuery](https://docs.cypress.io/guides/references/assertions#Chai-jQuery), [Sinon-Chai](https://docs.cypress.io/guides/references/assertions#Sinon-Chai), which are dependencies of Cypress.

### Mocking the Backend [TODO]

Use `cy.server` and `cy.route` to stub API responses.

```typescript
cy.server()
cy.route
```

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
