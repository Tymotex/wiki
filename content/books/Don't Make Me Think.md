---
title: Don't Make Me Think
description: Don't Make Me Think
---

> "The human brain's capacity doesn't change from one year to the next, so the insights from studying human behaviour have a very long shelf life. What was difficult for users twenty years ago continues to be difficult today." — Jakob Nielsen

> In the last few years, making things more usable has become almost everybody's responsibility. Visual designers and developers now often find themselves doing things like interaction design (deciding what happens next when the user clicks, taps, or swipes) and information architecture (figuring out how everything should be organised).

I've personally found this to be very true. Thinking about how to arrange user interactions and where to put UI components wherever it makes sense tends to be a huge frictional point during development.

Usability is defined to be a function of the following parameters:
- Useful — does it fulfil an important requirement?
- Learnable — do you have to think to know how to use it?
- Desirable — is it pleasing?

In English, usability is whether:
> A person of average ability and experience can figure out how to use the thing to accomplish something without it being more trouble than it's worth.

## Law #1 — Don't Make Me Think
Design decisions exist on a spectrum from *obvious* to *requiring thought*. Always prefer designs on the *obvious* side (a useful rule when disputing design conflicts with someone else).
![[books/assets/obvious-spectrum.png]]
Always make clickable things *obviously clickable*.

## Web Users Are Brain-Dead By Default
> Design for **scanning**, not for reading.

People execute a very surface-level auto-pilot search algorithm for what they need from your website. Unless their purpose is to actually read your web content (like reading the words of a blog post), they will only notice the most visually obvious parts of the page that signal some useful purpose to them, almost always clicking the first they encounter.
![[books/assets/user-scanning-webpages.png|400]]

People usually perform a depth-first search through your site, not a breadth-first search!
> "... several studies have shown that the back button is second only to clicking on links as the most used feature on the web." ([source](https://blog.httpwatch.com/2007/10/03/60-of-web-users-cant-be-wrong-dont-break-the-back-button))

Alternatively, people may immediately look for a search box and enter a query there.

People will always prefer to 'muddle through' any product in general, and only resort to reading instructions as a last resort.

### Web Conventions
Prefer taking advantage of web conventions. Eg. the brand name and icon should usually exist on the top left of a navbar.
> Innovate when you *know* you have a better idea, but take advantage of conventions when you don't.

### Visual Hierarchy
> A good visual hierarchy saves us work by preprocessing the page for us, organising and prioritising its contents in a way that we can grasp almost instantly.

### Visual Noise
Ruthlessly strip or de-emphasise the unimportant UI elements and text. 

**Krug's Third Law of Usability**:
> Get rid of half the words on each page, then get rid of half of what's left.

### Format Text
- Generously use informative heading text (h1, h2, h3, ...). This allows scanning for the part of the web page most interesting to the user.
- Keep paragraphs very short.
- Generously use bulleted lists.

## Navigation
Navigation serves two critical purposes: 
1. It tells you where you currently are.
2. It tells you what's here.

The web convention for navigation is to have something that looks like this at the top of every content page and to highlight on the navigator which page you're currently on:
![[books/assets/standard-site-header.png|500]]
- Always have a logo and/or distinguished typeface for the site ID. It should always take you home.
- Always keep the utility buttons minimal. Only show the most frequently used. The rest should be stowed away in the footer or in a different menu.

*All pages must have a name*, just as all streets have names and all intersections have street signs.
![[books/assets/page-name-examples.png|600]]

