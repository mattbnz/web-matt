---
title: "Effective on-call schedules must be flexible"
date: 2024-05-08T12:17:24+12:00
draft: true

categories:
  - Technology
  - Oncall
---

You will recall that I believe [on-call is a learning opportunity]({{< relref "2023-08-16-oncall-opportunity" >}}) not simply a burden to be borne.

Effective scheduling is the first foundation required to realise that opportunity. It's the best place to start because,
unlike most technical system changes, adopting a flexible on-call schedule can be accomplished quickly and delivers immediate benefits.


### Flexibility is key

The most important aspect of an effective on-call schedule is to minimise conflict between assigned on-call shifts and the many existing commitments
that place demands on our time and energy. Attempting to balance
time and attention between on-call and a conflicting committment adds stress to what is often an already stressful situation. That stress
not only lowers the effectiveness of the on-call response itself but contributes to the feeling that on-call is a duty rather than an opportunity to learn.

The common "industry standard" approach - round-robin assignment of shifts to team members in a fixed order - is as close to the worst possible method
of creating an effective on-call schedule as you could achieve. These rigid and inflexible schedules either ignore the cost of conflicting
commitments, or worse, expect members of the team to re-organise the rest of their life around the requirements of on-call!

Avoiding these outcomes and creating an effective on-call environment requires a **flexible schedule** that provides coverage for on-call shifts while
fitting around the existing committments and lives of the members staffing it.

Flexible on-call schedules lead to three major benefits for a team:
1. Barriers to entry to participate in on-call are lowered as team members gain confidence that on-call shifts will not interfere with other commitments in their life.
1. Stress levels during on-call shifts are reduced leading to improved outcomes as on-call responders can focus on the response without distraction from conflicting commitments.
3. Wide participation in low-stress on-call shifts provides a foundation upon which effective team practices can be established to drive iterative improvement and learning over time.


### Solving the flexibility challenge

Creating flexible assignments is much more complicated than using a fixed round-robin schedule due to the combinatorial explosion of potential shift
assignments that must be evaluated. Manual, human led planning of schedules is not possible. The need to maintain fairness and balance across team members
and between shifts adds further complications that must be considered beyond simply avoiding conflicting commitments. These challenges perhaps
partially explain why more widespread use of flexible on-call schedules are not observed.

From a software perspective the ability to solve these challenges is relatively straightforward using [constraint programming algorithms](https://en.wikipedia.org/wiki/Constraint_programming), but given the very human-centric nature of on-call scheduling the interface between team members and how information about
their commitments and other preferences gets into the scheduling system is a key part of the problem to solve.

This information needs to be obtained without requiring significant effort or extra maintenance - as important as on-call scheduling is to an effective on-call environment, it should be something that happens painlessly in the background, not
something that requires significant time or energy from anyone on the team to maintain.


### Calendar driven, constraint optimising scheduling

My experience from working with teams at Google and elsewhere, is that using an existing calendar as the source of on-call availability information
is the best approach. Calendars already contain many of the key events such as holidays and other out of office periods which are crucial inputs when building
a flexible schedule, and provide a simple, widely-available method for maintaining additional directives to the scheduling system by simply anotating existing
or newly created calendar events with basic "tags" somewhere in the title or description (e.g. no-oncall, prefer-oncall).

A flexible on-call scheduling system can be built by combining this calendar driven availability information (collected from each team member) with
configuration of the desired shift layout for a team. The resulting set of possibiltiies are scored by a constraint solving algorithm against the desired
criteria for the schedule (avoiding conflicts, balance, etc) and the optimum schedule found.

Teams can choose how far in advance they want this assignment process to run to strike a balance between maximising the amount of notice in advance of
being scheduled for a shift and the degree of forward planning of your calendar events that is required.

The result is flexible, effective on-call schedules with minimum effort and time required from the team. The perfect foundation from which to continue
building an on-call practice that delivers learning and growth!

### On-Call Optimizer

Flexible on-call scheduling that lowers barriers to entry, reduces stress levels and provides a foundation for iterative improvement and learning practices
to be established upon is a requirement for any team wishing to operate an effective on-call rotation.

The use of existing calendar information combined with
constraint solving algorithms provides a straightforward and no-hassle method of achieving this flexibility - but is not functionality that is available in
any existing on-call or incident management product available that I have found!

I've spent the last few months working with a set of initial users to prototype and test a tool (working name: [On-Call Optimizer](https://oncall-optimizer.com))
that fills this gap. If you'd like to join that list, please get in touch.

Finally, if you need any further encouragement to explore flexible on-call scheduling, consider this. Regardless of where you start from, every other challenge in
scheduling an on-call rotation, from shift arrangement to how you handle nights and weekends and even other aspects like on-call training become easier to manage
when you have the greater range of potential solutions to choose that flexible scheduling provides. I'm excited to share more thoughts on these topics in some
upcoming posts.

