---
title: CSS
description: CSS
---

*CSS* (Cascading Style Sheets) is a declarative language for describing document styling. Also see [[software-engineering/programming-languages/SCSS|SCSS]].

## Writing Maintainable CSS
Some simple guidelines for writing maintainable CSS code. See [MaintainableCSS](https://maintainablecss.com/).
- Prefer semantic class names.
    ```html
    <!-- Semantic -->
    <div class="searchResults">
    <!-- Not semantic -->
    <div class="red pull-down m-2">
    ```
    > "... use values that describe the nature of the content, rather than values that describe the desired presentation of the content"
- Stick with a naming convention like this:
    ```css
    .module[-component][-state] { ... }

    /* Examples: */
    .breadcrumbs-link { ... }
    .breadcrumbs-link-disabled { ... }
    .breadcrumbs-separator { ... }
    ```
- Avoid using IDs just as hooks for styling.
- Avoid undoing styling rules, eg. resetting styles provided by bootstrap or by another one of your CSS rules elsewhere.
- Write comments as if you were documenting regular program source code, *especially if you write rules that are meant to solve an issue*. CSS is usually a huge pain for people, so please remember to help your future self, and especially others working with your code.
