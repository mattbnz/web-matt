---
title: "On-call is an opportunity"
date: 2023-08-16T08:33:24+13:00
draft: true

categories:
  - Technology
---

On-call in software teams has a bad reputation. Niall Murphy's 2018 polemic, [Against On-Call](https://www.usenix.org/conference/srecon18europe/presentation/murphy) is well worth a watch if you need a refresher on the many reasons why the reputation is justified.

Despite the current reputation, on-call can and should be an activity that every software engineer participates in and finds some measure of fulfilment from. Similar to how [type 2 fun](#on-call-should-be-fun-of-the-type-2-kind) provides fulfilment after the fact even when not enjoyable in the moment.

Many people I speak with still report that on-call in their teams today doesn't provide any fulfilment and is simply seen as a necessary duty that must be borne. Unsurprisingly given this mindset many teams struggle to find sufficient people to provide on-call coverage for their services.

Let's consider how we might change that.


## On-call is inevitable

Software systems are [complex](https://en.wikipedia.org/wiki/Complex_system). We absolutely can and must do our best to engineer them to avoid failure and be robust in the face of known risks, but good engineering is not enough. Complex systems are dynamic, constantly [operating in a degraded mode](https://how.complexsystems.fail/#5) and even with the best engineering still rely on the activities of human operators to [keep the system within the bounds of acceptable performance](https://how.complexsystems.fail/#17).

Many of those activities can and do happen within the context of our day-to-day work, but surprises are inevitable in a complex system, and therefore so is the need for a response, often at inconvenient times. Even in a perfect world where magic or amazing engineering skills guarantee surprises occur only during business hours it is still desirable to avoid disrupting everyone's productivity in response.

These realities dictate that whether anticipated or not, any software team operating a production system will need an on-call role to be filled. By its nature (responding to surprises that are potentially negatively impacting the users of the system) the role will be stressful and no amount of engineering work or better software can eliminate the need for it.

Acknowledging the inevitability of the role's existence provides an obvious path to minimising and managing the stress involved through preparation, practice and processes, but there is also a deeper opportunity. Given the right environment, on-call has the potential to evolve from a burdensome duty into an effective method of gaining and maintaining expertise that makes us better engineers and expands the capability our our teams.


## Effective on-call requires support from every aspect of a team

Creating an environment that enables on-call to fulfil that potential requires consideration of how every aspect of a team supports effective execution of the role. Attempts to add on-call as a discrete, additional responsibility alongside other work will only contribute to continuing poor on-call experiences.

Integrating on-call into a team usually begins with consideration of how big surprises (often called incidents) are responded to. Incidents have high potential for harm and are rich sources from which to draw insight and learning. Clear incident management processes provide guard rails against the harm and can be a foundation upon which the insights and learning can be mined.

Incident management processes are a necessary start, but effective integration of on-call into a team also requires attention to all the time spent outside of incidents. This includes everything from the logistics and scheduling of an on-call rotation, monitoring and alerting health, training of team members to instil confidence in their ability to fulfil the role, effective practices for learning and distributing knowledge, the ability of the team to improve the system and many other aspects in between.

Underlying everything, the team must have, or be developing, a culture that values learning and provides support and encouragement. Nurturing that this culture and all the various aspects of investment required across the team cannot be justified when the perception of on-call is simply that it's a duty to be borne.


## On-call makes you a better engineer

Luckily that perception, although widespread, could not be further from the truth. Far from being just a duty, on-call is the best opportunity a software developer has to develop and hone their [expertise](https://how.complexsystems.fail/#13) with complex software systems and [how they fail](https://how.complexsystems.fail/#18).

Without this experience our individual and collective ability to safely and reliably develop software systems is diminished. Avoiding on-call - whether through outsourcing to a different set of people, or minimizing the time and energy we invest in our execution of the role may appear beneficial in the short-term, but ultimately lowers our overall software delivery performance and capability.

This is not a new argument. [Charity Majors](https://www.youtube.com/watch?v=p_paJ2PB4MY) and [Cindy Sridharan](https://copyconstruct.medium.com/on-call-b0bd8c5ea4e0) articulated similar themes back in 2018, and it's no accident that the list of capabilities the [Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339) book and [DORA reports](https://dora.dev/devops-capabilities/) describe as predictive of high performing teams overlap significantly with the tean capabilities and culture that delivers effective on-call.

The best software developers will always be those who use effective, fulfilling on-call practices as an opportunity for growth and development as they support their software in production.


## Checking the direction of travel

Understanding whether a teams culture and practices are delivering growth can be slow and hard to rigorously measure. I've found that whether participants report that on-call feels a bit like type 2 fun from the [the fun scale](https://sketchplanations.com/the-fun-scale) is a much better proxy to quickly establish whether a team is heading in the direction of fulfilling the potential of on-call or not.

![the fun scale](https://sketchplanations.com/api/dl?uid=the-fun-scale&width=600px#center "Image: sketchplanations.com")

On-call is never type 1 fun that's enjoyable in the moment. There's too much inherent stress involved for that. But when it fits the model of type 2 fun (a little painful in the moment but fulfilling to look back upon) it's highly likely that both opportunities described above are being fulfilled and the team will experience growth of expertise and fulfilment in on-call rather than seeing it as a burden.

If all on-call is providing is adrenalin rushes, or stories of pain there is still unfulfilled potential to realise the opportunity that on-call provides.


## Software that supports iteration and growth

Incident response management is an active field of software and continues to receive new investment. Unfortunately most of the existing products contribute to the problem of unfulfilling on-call through their very design! Their focus is on minimizing the impact and time taken to respond to incidents, but the practices implemented and the behaviours that are enabled reinforce the mindset that on-call is simply a duty to be borne before getting back to other work. The negative feedback loop this induces for development of improved practices is a major contributing factor to the slow rate of improvement in how on-call is perceived and experienced.

We can do better. It's not that I believe there's a different or improved product whose use will immediately transform the on-call experience. Software doesn't automatically fix problems - particularly problems like on-call which interact with every aspect of a team.

Change only happens through [committing to a goal and iterating towards it](https://dora.dev/devops-capabilities/cultural/devops-culture-transform/#set-goals-and-enable-team-experimentation). Software can be a key tool for achieving that iterative cycle by enabling and encouraging desired new behaviours and making them easy to perform.

To realise the potential of on-call, the types of behaviours that need to be enabled are those that minimise the harm and stress associated with on-call and facilitate learning and knowledge sharing **throughout the lifetime of a team, not just during on-call shifts and incident response.**

## A product opportunity

The opportunity I see is to surround existing incident response processes with capabilities for flexible scheduling, easy straightforward shift swaps, a clear curriculum and training programme and straightforward analysis and sharing of knowledge.

A product that combines those capabilities together in an lightly opinionated way to nudge a team towards an iterative cycle of behaviour that not only solves the pain points of the current on-call experience, but drives improved software delivery performance as their expertise grows over time would have great value to many teams.

Someone should build this.

Maybe me? The problem space certainly fits my criteria of [solving a problem in my area of expertise]({{< relref "2023-mid-year-review.md#the-next-few-months" >}}), but is it a problem that enough people will pay good money to solve?

I've spoken to a variety of people in a range of companies over the last month, which has provided useful validation of the opportunity and insights into the variety of perspectives and appetite to address it. The next step is to pitch a more detailed description of the product above and see if it's compelling enough to drive some commitments.

Watch this space for updates on whether that's successful!