---
title: Konflux
---

1. Learn Dart and Flutter!
    1. ~~Set up Flutter and get the hello world app working on physical Android.~~
    2. ~~Complete the **Build your first flutter app** 2 codelabs. Take notes as you go.~~
2. ~~Need to understand the problem I’m solving, and then ideate solutions~~
3. ~~How are shareable and persistent links implemented?~~
4. ~~Need to have a UI design in Figma sorted before actually producing styling UI.
Good time to learn Figma a little more deeply.~~
5. ~~Needs MVP definition and launch date.~~
6. ~~Learn Firebase auth.~~
7. ~~Learn Firebase DB~~
8. ~~Needs architecture planning (backend). I really need to understand enterprise application architecture… but this isn’t necessary for an MVP.~~
9. ~~Needs a GitHub project.~~
10. Learn marketing, sales and app business strategy.

---

Challenges:

- NoSQL data model design:
    - Data access speed and data redundancy tradeoff.
    - Denormalisation/normalisation.
- User flow:
    - It’s important to get it right the first time, else you’ll move stuff around unnecessarily and waste time.
    - Should’ve ran through a complete user flow in my prototype and critiqued it before I built it out. I wasted time iterating on it as I developed the code instead of iterating on it through Figma.
- Wasted so much fucking time on working with the data models… I need to figure out the data flow properly.

---

## Requirements

**The problem**:

*Informally:* 

Whenever I want to arrange a meetup with friends as a university student with a loaded schedule, the main frictional point is finding a common time that the people I’m inviting are available. The main solution to this currently, as far as I can see, is When2Meet. The other alternatives tend to be heavyweight, like Calendly, Doodle, etc. I only ever used When2Meet because you could arrange events by quickly filling in availabilities **without an account** and then quickly distribute a link for others to see the group’s availabilities.

When2Meet works for simple events, but there are no features for event management. When you’re looking to organise something, you’re responsible for not losing the link you distributed. 

Every time you arrange an event, you must fill in your schedule completely, again, which is cumbersome and challenging to sync, especially since availabilities are not static.

No details exist about the event beyond the times and attendees.

When an event is arranged, you’re still responsible for manually putting it into Google Calendar.

**Competitors**:

- When2Meet.
    - Not responsive on mobile. No app.
    - Doesn’t let you expand/shrink the time after defining the time range for an event.
- Calendly.
- Doodle.
- [https://lettucemeet.com/](https://lettucemeet.com/)
    - Nice guided usage

Konflux will have superior UX and a very lightweight UI and user flow that is only marginally more complex than When2Meet.

**Target audience**:

Targeted towards busy adults and uni students who struggle with finding a window of time for meeting up socially. It would be too hard to challenge business scheduling since there are too many mature competitors. The main difference in targeting uni students and young adults looking to arrange smaller social meetups is that they are not going to adopt a heavyweight system like Calendly, however a very minimal system like When2Meet lacks a lot of quality of life features.

**Business model**:

TODO. Premium features? Scaling features (eg. manage more than 3 events)?

**Features**:

Remember, I need to have a clear line of reasoning for the business value of each feature. Iteration 1 features constitute the MVP and are highlighted blue.

- When2meet feature set:
    - Time range selection and modification. It should be possible to expand the time range and shrink it easily.
        - Days of the week.
        - Over the next 30 days.
    - Shareable and persistent link.
- Event management:
    - Locally persistent events list.
    - Selecting the venue and showing the location on an embedded map (Google Maps).
    - Showing the weather forecast for each timeslot and chance of rain.
        - Note: could do a linear gradient with each timeslot’s datapoint and interpolate the colours smoothly with chroma
    - Superimposed calendar visualising all your events.
    - Show an expected time to destination for all invitees based on their address so that everyone gets there on time.
    - Allow the organiser to set a list of preparatory things prior to the event (eg. bring sunscreen, etc.)
    - Setting polls (which can be anonymised).
    - Single, multi-day and recurring events.
    - If there are no time slots where everyone is free, there should be a way to prompt an invitee to revise their availability (since we might put a very conservative schedule).
- An authentic and aesthetic mobile experience that feels very polished and stylish.
    - Guided slideshow-like initial navigation.
- Notifications through email.
- Notifications through SMS.
- ‘Share to Messenger’
- Setting deadlines and reminders for when invitees need to fill in their schedule by.
- Smarter scheduling (the goal should be to minimise the amount of thought that needs to go into picking the best time):
    - Highlighting the times with the best weather.
    - Highlighting opening/closing times of the target venue (is this possible through some API? Google Maps?)
- Timeweave feature set (this was a pretty popular app but was simply always broken…):
    - See who else you’ve *added* is currently available, or will become available.
- Timezone support.
- Automatically recommends event times and ideas based on past venues. You specify that you want to meet person B sometime over next week, then the app suggest exactly when and where.
Presents a list of ideas. 
This would be great for dates.

## Iteration #1

The purpose of iteration 1 is to ship something that does everything When2Meet does, *but with slightly better UI and UX* and event persistence.

**Deliverables**

1. Low-fidelity Figma prototype.
2. Minimally styled React/Next/TS/SCSS web client that mostly implements the Figma prototype for the core iteration [#1](https://github.com/Tymotex/Konflux/issues/1) feature set.
3. Firebase DB services setup.

**Architecture/Deployment**Extremely simple. Just deploy the Next.js client to Vercel.

**Feature Set:**

- When2meet feature set:
    - Time range selection and modification. It should be possible to expand the time range and shrink it easily.
        - Days of the week.
        - Over the next 30 days.
    - Shareable and persistent link.
- Event management:
    - Locally persistent events list.

**Production Checklist:**

- Should I limit the number of people in an event? Eg. 20 people?
- For how long should the event persist in the database before being erased? 20 mins?
- Should have an error logging service dashboard that I can view.
- Should have an uptime and traffic monitoring service dashboard that I can view.
- Protect sensitive user info in Firebase.
- How am I going to get user feedback for this?

## Iteration #2

## UI
Talloc:
![[Projects/Konflux/assets/talloc.png|500]]