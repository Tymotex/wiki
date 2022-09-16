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
- Delightful
- Desirable — is it pleasing?

In English, usability is whether:
> A person of average ability and experience can figure out how to use the thing to accomplish something without it being more trouble than it's worth.

## Don't Make Me Think
Design decisions exist on a spectrum from *obvious* to *requiring thought*. Always prefer designs on the *obvious* side (a useful rule when disputing design conflicts with someone else).
![[Reading/assets/obvious-spectrum.png]]
Always make clickable things *obviously clickable*.

## Web Users Are Brain-Dead By Default
> Design for **scanning**, not for reading.

People execute a very surface-level auto-pilot search algorithm for what they need from your website. Unless their purpose is to actually read your web content (like reading the words of a blog post), they will only notice the most visually obvious parts of the page that signal some useful purpose to them, almost always clicking the first they encounter.
![[Reading/assets/user-scanning-webpages.png|400]]

People usually perform a depth-first search through your site, not a breadth-first search!
> "... several studies have shown that the back button is second only to clicking on links as the most used feature on the web." ([source](https://blog.httpwatch.com/2007/10/03/60-of-web-users-cant-be-wrong-dont-break-the-back-button))

Alternatively, people may immediately look for a search box and enter a query there.

People will always prefer to 'muddle through' any product in general, and only resort to reading instructions as a last resort.

### Web Conventions
Prefer taking advantage of web conventions. Eg. the brand name and icon should usually exist on the top left of a navbar.
> Innovate when you *know* you have a better idea, but take advantage of conventions when you don't.

Facebook, for example, popularised the usage of the hamburger icon. Leverage this convention to tuck away seldom used features behind the menu.
![[Reading/assets/hamburger-menu-icon.png|100]]

### Visual Hierarchy
*Visual hierarchy* is the arrangement and styling of elements on a webpage according to their importance. You use this to control the order of elements in which the user's eyes scan through on the webpage.

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

### Primary Navigation
The web convention for navigation is to have something that looks like this at the top of every content page and to highlight on the navigator which page you're currently on:
![[Reading/assets/standard-site-header.png|500]]
- Always have a logo and/or distinguished typeface for the site ID. It should always take you home.
- Always keep the utility buttons minimal. Only show the most frequently used. The rest should be stowed away in the footer or in a different menu.

### All Pages Must Have Names
*All pages must have a name*, just as all streets have names and all intersections have street signs. It must be present on the document and given emphasis, and not just only present in the tab's name or highlighted in the navigation UI.
![[Reading/assets/page-name-examples.png|600]]

### Breadcrumbs
Breadcrumbs are concise navigators that don't contribute much visual noise to a page. Here are some best practices:
1. Place it at the top.
2. Use the right chevron › to separate parts of it.
3. Highlight the last breadcrumb.

## Homepage
Homepages must make clear *what the site is*. They are responsible for creating the first impression and generating traffic towards other subpages.

**Note**: yes, it's unlikely that a large amount of traffic begins from the homepage (instead, it'll be from direct links to subpages from Google search results, for example), but often people will navigate to the homepage if they find the content on the subpages interesting. You still need to get the homepage right.

**Things to have**:
- The primary navigation at the top, including the site ID, utility buttons and navigation buttons.
- A tagline, typically sitting right under or next to the site ID. Know the difference between a [tagline and a motto](https://chevronediting.com.au/tagline-motto-slogan-difference) however.
- A welcome blurb.
- A learn more link to a page with the finer details.
- An embedded demo video of the product or business.

Don't crowd the homepage with too many leads, especially promotions.
> "Any shared resource will inevitably be destroyed by overuse." (see the [Tragedy of the Commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons))

## Usability Testing
Usability tests involve getting users individually to try out the website/app/product, seeing how they feel about it and if it solves their problems, and noting what problems they run into.

> After you've worked on a site for even a few weeks, you can't see it freshly anymore... The only way to find out if it really works is to watch other people try to use it.

> Testing one user early in the project is better than testing 50 near the end.

> Every web development team should spend **one morning a month** doing usability testing.

For each of those usability testing sessions, just get 3 people to use your website. Give them a list of tasks to do using your website, observe them, then take notes. The goal is to get actionable insights, not conduct a scientific experiment that would require a large sample size.
- Those 3 people need not be from your target audience. They will still run into usability problems.
- [There are strategies for finding users](https://www.nngroup.com/reports/how-to-recruit-participants-usability-studies/). The simple way is to ask your friends and acquaintances, or post an ad somewhere. Offer a decent stipend.
    - You can use unmoderated remote testing like [UserTesting](https://www.usertesting.com/).

### Design Disputes
Everyone has their own concept of what UI is pleasant to use and what UI is not. 
> "All web users are unique. And all web use is basically idiosyncratic."

The only antidote to resolving design disputes about what UI to use and how it should be designed is to build out a crude version and give it to users for testing.

## Affordances
An *affordance* is a set of visual cues in an element that imply the usage of that element.
![[Reading/assets/affordance.png|500]]

## Goodwill
In addition to designing sites that don't make you think, you should strive to make design decisions that are 'kind' to your user.

Some examples not-so-kind practices:
- Making you sign up *after* doing something time-consuming. Eg. if you've used some online video editor, you might have been prompted to make an account after you've made your *edits*. Sometimes they may even charge you to download your edited video.
- Forcing you to supply personal details when signing up.
- Incessant popups.
- Hiding, de-emphasising or prefilling a button or input that they don't want you to click/change. Eg. automatically checking the 'subscribe me to all marketing emails' button.

Some examples of kind practices:
- Show all important information upfront, like fees, rather than hiding them away further along some process and exploiting the user's feeling of sunk cost.
- Providing *real* FAQs.
- Preventing common errors. My personal favourite is Gmail's warning popup that you might have forgotten to make an attachment.
    ![[Reading/assets/gmail-attachment-warning.png|450]]


