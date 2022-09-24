---
title: CSS Cookbook
---

A collection of tricks and common things to achieve with [[Knowledge/Engineering/Languages/CSS|CSS]].

## Centering
[Complete guide to centering](https://css-tricks.com/centering-css-complete-guide/).
- **Centering horizontally**:
    - Inline? `text-align: center` on the parent.
    - Block? `margin: 0 auto; width: 200px`.
    - Multiple blocks? `display: flex; justify-content: center`.
    - Hack: 
        ```css
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    ```
- **Centering vertically**:
    - Inline (text)?: 
    ```css
    .center-text {
        height: 100px;
        line-height: 100px;
        white-space: nowrap;
    }
    ```
    - Block?
    ```css
    display: flex;
    flex-direction: column;
    justify-content: center;
    ```
    - Hack: 
        ```css
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    ```

## Responsive
- [Fluid images](https://unstoppablerobotninja.com/entry/fluid-images/) to prevent images from ever overflowing: `img { max-width: 100%; }`. 


