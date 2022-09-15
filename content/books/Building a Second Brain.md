---
title: Building a Second Brain
---

## Summary
Your 'second brain' is a lifelong system serving as a knowledge repository, a place to manage the projects that are important in your life, and a place to steward your personal growth.

💎 Note-taking is an investment into an asset that serves your future self. The distillation of an idea is what makes an insight useful to your future self.

*Finished first reading on 15th September, 2022*.

## Reflection
Organising is easily the most difficult part of personal knowledge management for me. I find that I simply never return to notes after writing them, so unfortunately I'm never capitalising on my hard work. I've always organised things hierarchically and have endlessly wrestled with the question of where to put this new thought I had or this inspiring tidbit I read from an article or blog post.

---
## Information Overload and Mismanagement
> We consume more books, podcasts, articles, and videos than we could possibly absorb. What do we really have to show for all the knowledge we've gained? How many of the great ideas we've had or encountered have faded from our minds before we even had a chance to put them into practice?

Even after more than 3 years studying computer science rigorously, I have little to show for it. I've taken notes, but I rarely ever view them more than once. I never captured and organised my notes in a way that sought to serve my future self. Similarly, I've consumed a number of self-help books, hundreds of hours of podcasts and insightful YouTube videos. If put on the spot, I would not be able to explain for more than a few minutes all the value I've derived from this information.

> A report from the International Data Corporation found that **26 percent** of a typical knowledge worker's day is spent looking for and consolidating information spread across a variety of systems.

I found this statistic to be believable based on my experiences in internships and personal life. Every time I sat down to work on a project, whether personal or for work, I had to load all the context of the project into my working memory first, much like how running a process on a computer requires the program's instructions and data to be loaded onto RAM before running. Consolidating information in one place in a system you can trust will help to reduce the time taken to load the instructions and data into your biological brain.

The significant overhead of looking for information and transitioning into the focused state of mind required to execute on your best work is something discussed thoroughly in Cal Newport's book, 'Deep Work'. A second brain is one helpful strategy for reducing the friction associated with starting and resuming work on mid-term and long-term projects.

## Creativity
One thing this book has taught me is that creativity is not some nebulous, innate quality of a person. Instead, it is a principled, disciplined, long-term process 
> In its most practical form, creativity is about connecting ideas together, especially ideas that don't seem to be connected.

> Innovation and impact don't happen by accident or chance. Creativity depends on a *creative process*.

Creativity is not something you can manifest out of the void. It is a process fuelled by the connection of existing thoughts that surface.

About writer's block:
> "It's not that I'm blocks. It's that I don't have enough research to write with opwer and knowledge about the topic. It always mens, not that I can't find the right words, [but rather] that I don't have the ammunition." — Sebastian Junger, author and filmmaker

### Divergent and Convergent Thinking 
![Divergent vs. convergent thinking](books/assets/divergent-convergent-thinking.png)
([source](https://www.wrike.com/blog/convergent-thinking-vs-divergent-thinking/))

When undertaking creative problem-solving, you'll go through cycles of divergence (the research and chaotic generation of a lot of ideas) and convergence (the pruning/distillation/selection of the choices to create the final product). The *capture* and *organise* part of CODE is divergence, while *distillation* and *express* is convergence.

As a software engineer, this really aligns with the value of *prototyping*. You have a problem to solve but you tinker with a very open mind to produce a barebones part of the solution. When it comes time to converge, you enter a hyperfocused state of deep work, ruthlessly ignore distractions and get the project implemented and shipped.

In some way, the divergence and convergence model is basically another expression of the *explore and exploit* tradeoff.

One thing this book has convinced me of is that creativity is principle-based.

### Archipelago of Ideas
A way to counteract writer's block is to start from a point of abundance rather than scarcity.
> "Instead of confronting a terrifying blank page, I'm looking at a document filled with quotes: from letters, from primary sources, from scholarly papers, sometimes even my own notes. It's a great technique for warding off the siren song of procrastination. Before I hit on this approach, I used to lose weeks stalling before each new chapter, because it was just a big empty sea of nothingness. Now each chapter starts life as a kind of archipelago of inspiring quotes, which makes it seem far less daunting. All I have to do is build bridges between islands" — Steven Johnson

## CODE
On the encountering of new information:
1. C, *capture* — keep what resonates. Be judicious and select the most noteworthy ideas you encounter. They should evoke curiosity or some kind of a-ha moment.
	> Adopting the habit of knowledge capture has immediate benefits for our mental health and peace of mind. We can let go of the fear that our memory will fail us at a crucial moment. Instead of jumping at every new headline and notification, we can choose to consume information that adds value to our lives and consciously let go of the rest.
	
	> As you consume a piece of content, listen for an internal feeling of being moved or surprised by the idea you're taking in.

	> I can't think of anything more important for your creative life, and your life in general, than learning to listen to the voice of intuition inside. It is the source of your imagination, your confidence, and your spontaneity.
2. O, *organise* — save for actionability.
	> The best way to organise your notes is to *organise for action*, according to the active projects you are working on right now.

	> One of the biggest temptations with organising is to get too perfectionistic, treating the process of organising as an end in itself.

	> The temptation when initially capturing notes is to also try to decide where they should go and what they mean.

	Don't make organising your second brain a heavy obligation - you likely have enough of those.

	To organise for actionability, determine which bucket the idea falls in using PARA:
	1. **P**rojects — the discrete, big things in your life you're working on currently with a clear beginning and ending. Examples:
		- Plan vacation to Cairns.
		- Complete C++ book.
		- Buy new noise-cancelling headphones.
		- Write a blog post.

		Knowing what your projects are helps you easily identify and say no to the things that don't move you forward. Expect to have around 5 projects at a time. What your projects are is a reflection of your identity and what you're committed to achieving.
	2. **A**reas — long-term responsibilities that don't have a clear endpoint, but which you might have a general standard to achieve (eg. spend more time with family, keep cholesterol below some amount, etc.) Examples:
		- Nutrition
		- Powerlifting
		- Personal finance
		- Software engineering
		- Stoicism
		- Writing
		- Reading
		- Typing
		- Meditation
	3. **R**esources — ideas and notes for future you. Anything that doesn't fall into projects or areas lands here. It encompasses a broad range of miscellaneous things that you have an interest in but which won't serve you at this moment. Eg. notes on coffee-brewing, Freud, leadership, nutrition, fishkeeping, philosophy, gifts, travel, etc.
	4. **A**rchive — completed projects and anything in projects, areas or resources that you no longer have an interest in. 
		You can satisfy both your hoarding tendencies and minimalist ideals by shoving things into the archive, knowing they're out of the way and that they'll still be there forever.

	Forcing yourself to decide where a new note goes introduces friction to the capturing process.
	Organising should be done separately and according to the following algorithm:
	```C
	if (belongs in project p) placeInProject(p);
	else if (belongs in area a) placeInArea(a);
	else if (belongs in resource r) placeInResource(r);
	else placeInArchive();
	```

	Stop thinking about your second brain as a wiki or library. Think instead of it as a production system. Consider about how kitchens are usually organised - you don't organise them based on alphabetical categories of 'fruits', 'vegetables', 'dairy', etc., instead you'd be better off organising the kitchen to support your timely, frictionless cooking of meals.

1. D, *distil* — find the essence and write the main takeaways. You should think: "how can I make this as useful as possible for my future self?" 
	> Every idea has an "essence": the heart and soul of what it is trying to communicate.

	Be a curator. **Ruthlessly** strip down the article or book you're reading and only choose to save the important stuff.
	> In any piece of content, *the value (to you) is not evenly distributed*.
	
	> Prune the good to surface the great.

	Consider recursively filtering your notes and extracting out a bullet-point list for an executive summary (in your own words!) to be placed at the top of your notes. When reading a book or article, note the highlighted passages, then highlight again the top few most important previously highlighted passages to get the most impactful takeaways.

	The author recommends 'progressive summarisation' where you emphasise your notes in tiers. Eg. bold text for notable parts and highlight a subset of the bolded text for the critical insights. Highlighting in tiers means you can review the note and only read the critical insights when pressed for time.

	**Investing in your future self**:
	While capturing and organising should be extremely frictionless and unambiguous to do, distilling will take time and effort investment. You should always assume by default that something you're reading is not useful enough to highlight. The purpose of distillation is to serve your future self.
	
	In taking notes mindfully with the intent of projecting forward the most intriguing thoughts to your future self, you are *deliberately practicing* your distillation skills, and by extension, your communication skills. Occasionally try to open a note sometime in the past and see how effective your distillation skills were. If you can grasp the idea within 30 seconds, you've done a good job.

	Distilled notes are far more *discoverable* than raw notes. A note with low discoverability is significantly less useful to your future self. Each time you distil an idea, you are investing in an asset that has the potentially to continuously output value.

	> When the opportunity arrives to do our best work, it's not the time to start reading books and doing research. *You need that research to already be done*.
	
1. E, *express* — show your work.
	> A common challenge for people who are curious and love to learn is that we can fall into the habit of continuously force-feeding ourselves more and more information, but never actually take the next step and apply it.
	
	For instance, at this moment I've read books on entrepreneurship and dating, neither of which I have made steps to doing (because I keep rationalising about myself being lacking in knowledge and time).

	> **Shift as much of your time and effort as possible from consuming to creating**.

Claude Shannon describes information as 'that which surprises you'. Beware of confirmation bias, you should capture things that go against your understanding rather than only capturing things that reinforce it.

You should be writing things in your own words as much as possible. The **generation effect** is a memorisation phenomenon where actively producing material leads to better retention than simply reading and copying content passively.

> It doesn't matter how organised, aesthetically pleasing, or impressive your notetaking system is. It is only the steady completion of tangible wins that can infuse you with a sense of determination, momentum, and accomplishment.

Stop thinking of your personal knowledge system as static. You live your life in seasons, and your second brain should be a supplementary parallel of your first brain. Since you know that the archive is kept forever and readily searchable, don't be afraid to ruthlessly evict and strip projects, areas and resources notes.
> "To attain knowledge, add things every day. To attain wisdom, remove things every day." — Lao Tzu

Notes are meant to be used, not collected.

> Professional creatives constantly draw on outside sources of inspiration - their own experiences and observations, lessons gleaned from successes and failures alike, and the ideas of others.

> As knowledge workers, attention is our most scarce and precious resource.

... and we live in a distracted world. This is why meditation is such an enriching experience. 

> It is by sharing our ideas with other people that we discover which ones represent our  most valuable expertise.

I realised that I severely lack this in my life. Outside of my internship and the assignments I've submitted at university, I've never had the quality of my output judged by other people. This realisation, among many other motivations, has prompted me to pursue blog writing as a pastime.

> Our knowledge is now our most important asset and the ability to deploy our attention our most valuable skill.

Having a Second Brain lets you manage thoughts of anxiety, knowing that all your important ideas are captured and that you're making progress through your projects and growing as a person. Isn't it a powerful feeling, knowing that you're pursuing projects backed with a huge repository of knowledge you've built up over years and that they're all aligned with lifelong goals?

## Blog Writing

> Life has given you a set of experiences that provide you with a unique lens on the world. Through that lens you can perceive truths that can have a profoundly positive impact on you and others.

> Finding your voice and speaking your truth is a radical act of self-worth: Who are you to speak up? Who says you have anything to offer? Who are you to demand people's attention and take up their time?

