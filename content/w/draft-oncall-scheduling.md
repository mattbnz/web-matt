---
title: "Effective on-call schedules must be flexible"
date: 2024-05-08T12:17:24+12:00
draft: true

categories:
  - Technology
  - Oncall
---

As previously discussed, on-call is an opportunity to become better at our jobs not simply a burden to be borne. This post begins the next step
in explaining how to realise the opportunity: an effective on-call schedule.

While effective scheduling is only one of the key foundations for creating an on-call environment that delivers growth in a team, it's the best place to start when you want to drive improvements. Unlike technical system changes
adopting a flexible on-call schedule can be accomplished quickly and delivers immediate benefits.


### Flexibility is key

The most important aspect of an effective on-call schedule is to avoid minimise conflict between assigned on-call shifts and the many existing commitments
that place demands on our time and energy. Attempting to balance
time and attention between on-call and a conflicting committment adds stress to what is often an already stressful situation. That stress
not only lowers the effectiveness of the on-call response itself but contributes to the previously discussed perception that on-call is simply a
burdensome duty.

The current "industry standard" on-call scheduling approach of round-robin assignment of shifts to team members in a fixed order is
almost a perfect example of how not to create an effective on-call schedule. These rigid and inflexible schedules either ignore the cost of conflicting
commitments, or worse, expect members of the team to re-organise the rest of their life around the requirements of on-call!

Avoiding these outcomes and creating an effective on-call environment that can deliver growth in expertise requires a **flexible schedule** that achieves
the necessary assignment of shifts in a way that fits around the existing committments and lives of the members staffing it. Flexible on-call schedules
lead to three major benefits for a team:

1. Barriers to entry to participate in on-call are lowered as team members gain confidence that on-call shifts will not interfere with other commitments in their life.
1. Stress levels during on-call shifts are reduced leading to improved outcomes as on-call responders can focus on the response without distraction from conflicting commitments.
3. Wide participation in low-stress on-call shifts provides a foundation upon which effective team practices can be established to drive iterative improvement and learning over time.


### Solving the flexibility challenge

The fact that inflexible round-robin schedules continue to be the most common approach to on-call scheduling despite the benefits that
more flexible schedules would provide hints that there are some challenges to be overcome in achieving this foundation.

* Moving from a fixed round-robin schedule to flexible assignments reveals a combinatorial explosion of potential schedules even for small
teams. Manual, human led planning of flexible schedules is not sustainable.
* Flexible schedules lack the predictability of round-robin assignments. The simplicity of knowing that you will be on-call every Nth week without
having to explicitly look at the schedule is valued by many people, even when faced with the inevitable conflicts it produces.
* Data availablity and cost. Achieving flexible schedules requires accurate data about existing commitments to avoid for each member of the team, which
must be accurate and obtainable at low cost - primarily in terms of team member time. No-one wants to spend significant amounts of time planning on-call
shifts.
* Maintaining fairness and balance across team members and between shifts is more complicated when flexible schedules are in-use, adding to the cost of
managing the combinatorial explosion of potential schedules.

The only way to overcome all these challenges is through software that is able to automatically sort through the many potential combinations of shift
assignments and find the optimum schedule that minimizes conflicts while maintaining all the other desired properties.

The best source of data for the commitments of each team member is usually their calendar which already contains key events such as holidays and other out
of office periods which are crucial to building a schedule. For further flexibility simple text-based tags (e.g. no-oncall, prefer-oncall) can also be used
to provide further input data to the scheduling system at the same time as the underlying events are created/modified on the team members calendar.


### Calendar driven, constraint solving scheduling

In my experience this combination of calendar driven data with a constraint optimising scheduling tool is the best way to provide a flexible on-call
schedule for a team. You obtain all the benefits of a flexible schedule for a very minimal level of overhead spent on ensuring the appropriate tags
and out of office events are present in your calendar(s).

Each team can choose how far in advance they want their schedules generated to strike a balance between maximising the amount of notice in advance of
being scheduled for a shift and the degree of forward planning and calendar maintenance that must be sustained. I've seen some teams using daily on-call shifts schedule only 1 week in advance once they're comfortable with the process!

The tooling to achieve this type of scheduling outcome was simple and easy to use at Google, but is not possible in any of the existing incident management
and on-call products on the market today.

I've spent the past few months building and testing a product to solve this gap with some early customers - watch this space for more news soon!