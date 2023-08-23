---
title: "What is on-call?"
description: Practical foundations for a discussion of what's required to realise the opportunity on-call presents.
date: 2023-08-23T15:37:24+13:00

card_image: oncall-opportunity.jpg

categories:
  - Technology
---

On-call as an [opportunity for growth and learning]({{% relref "2023-08-16-oncall-opportunity.md" %}}) in a team is a powerful vision to aim towards, but a vision without a practical path towards achievement is not very useful.

This post aims to step back from my lofty ideals of what on-call can achieve and build some common ground around two basic aspects of on-call: what it is we're actually talking about and the roles and responsibilities of the different people involved.

From that foundation, future posts will then dive into more details on how specific aspects of a team's environment can be nurtured to make practical, incremental progress on the journey towards fulfilling on-call.


 ## Mental models of on-call

I claimed that on-call is inevitable, needs support from all aspects of a team and is more than just incident response. Each statement is true, but like [blind men describing an elephant](https://thesystemsthinker.com/the-blind-men-and-the-elephant/), don't really answer the question of what on-call actually is.

Rather than spending time trying to actually define on-call, I think it's more useful to lean into the concept of a mental model of on-call as a guide. Every team and each of us individually has a different experience of on-call that shapes perceptions of what is or isn't or should or shouldn't be involved in the discussion. Some aspects of those models have positive characteristics that we'd like to see more of, others are negative. There's no absolute right or wrong model of on-call, each model can teach us something about how to apply on-call to our unique context, but only if we realise the our models are different!

The mental model I primarily use to think about on-call is based on the landscape of work that a software team is faced with organised along two axes giving four quadrants - for me on-call is roughly consistent with the bottom right quadrant.

- X-axis: urgency of response (months, weeks, days, hours, minutes)
- Y-axis: size of response (single person, few people, whole team, whole company)

 On the horizontal axis we have the urgency or desired deadline for when the work must be completed, ranging from months on the left, through week, days and hours to end up with minutes on the right. On the vertical axis we have the number of people directly involved in completing the unit of work, ranging from a single individual at the bottom, through small groups and teams up to the entire company at the top.

 On-call occupies a space roughly consistent with the bottom-right of this quadrant, bounded by days on the left, and multiple below above. Requiring an urgent (hours to minutes) response, but within the scope that one or maybe two people can resolve. On the very left of the spectrum is our planned work, governed by our goals and objectives. In the bottom middle is other operational work - often called bugs or tickets, and in the top right are incidents - urgent situations requiring a large, co-ordinated response.

## Implications of my mental model

- Focused on the work to be done, not how to do it.
- Compared to the other quadrants, it's notable how little existing framework/structure/discussion exists around on-call

## Who's job is it to create a fulfilling on-call environment?

Who is the audience for these posts? Who am I trying to convince. It's relevant to everyone working with software products, but primarily towards leaders at both the team and organisational level.

Culture is how we act, not what we say. Members of a team have a huge influence on the culture in teh team, regardless of what the leadership intends.

But leadership can either make that change easier or harder, and change will occur much quicker with leaderhsip buy-in and support, so


## What can you do

Leadership has more leverage, but that doesn't mean you're powerless as an individual team member participating in on-call.


. Discussion of potential improvement requires a clear understanding of what requires clarity on the desired goal or destination. Equally, simply stating the opportunity
Now that we understand the opportunity on-call presents it's time to come down from the lofty heights of idealism and get into the nitty gritty of what realising that opportunity actually looks like.

This post is about establishing some common ground for more concrete discussions of what relaising that opportunity will look like in a team.

We're going to cover:

* What is on-call anyway?
* Who's responsibility is it?
* What to do if you don't have leadership support?
* Peek into coming topics


## On-call lacks structure and guidance

In addition to the labels and names we commonly give to the work in each of these quadrants we could also list the established frameworks and ways of working that are used to improve performance:


, for example:
- incident response: PD guide, incident response procesess
- programs: agile, scrum, kanban
- tasks, projects: GTD, pomodoro

But can you think of similar examples that exist to What exists in the bottom right corner to provide similar structure and guidance? I can't.

I don't have a fancy name or brand, but I do think there is a topic worth exploring and discussing further here what are the practices and actions that we take in our team that relate to the day-to-day on-call work in this quadrant.
