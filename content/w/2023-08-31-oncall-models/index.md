---
title: "Mental models of on-call"
description: Establishing common ground for a practical discussion of how to realise the opportunity on-call presents.
date: 2023-08-23T15:37:24+13:00
draft: true

card_image: oncall-opportunity.jpg

categories:
  - Technology
---

Productive discussion of how to realise the [opportunity offered by on-call]({{% relref "2023-08-16-oncall-opportunity.md" %}}) requires understanding the different experiences and mental models of on-call that exist in the world.

This post aims to step back from high-level discussion of the opportunity on-call offers to focus on explaining two key mental models I use to think about on-call and the roles and responsibilities of the different people involved.


 ## What is on-call?

Beyond the simplistic understanding of on-call being responsible for fixing something when it breaks, I find that looking at where on-call sits in the broader landscape of work involved in developing and operating a software system provides a more complete understanding of what's involved.

![on-call work model](oncall-what.png#center "The landscape of software work. Apologies for the rough diagram.")

 On the horizontal axis is the time window within which the work must be completed, from months on the left to minutes on the right. On the vertical axis is the number of people directly involved in completing the unit of work, from a single individual at the bottom up to the entire company at the top.

 On-call occupies a space roughly consistent with the bottom-right quadrant, bounded by days on the left, and multiple people above. Requiring an urgent (hours to minutes) response, but within the scope that one or two people can resolve.

This framing of on-call shows why responsiveness is key, but also explains why [on-call is inevitable]({{% relref "2023-08-16-oncall-opportunity.md#on-call-is-inevitable" %}}) (there will always be work falling in this quadrant regardless of whether you want it to or not) and why [on-call and incident response require distinct planning and preparation]({{% relref "2023-08-16-oncall-opportunity.md#the-narrow-scope-of-existing-tools" %}}) (they handle different scales of event and response).


## Who should be on-call?

In an ideal world everyone developing software would benefit from the opportunity for growth and development that on-call provides, but "you build it, you run it" won't deliver results in practice if the engineers developing the software are not provided with an effective and supportive environment.

Creating that environment requires balancing the ideal of developers being directly on-call for the software they write against constraints such as minimum rotation sizes, sufficient knowledge of the systems supported and many other factors, all of which are in some amount of tension with each other.

The solution to this problem will look different in every situation. There is no single model of on-call staffing or rotation structure that must be followed, but that does not mean the structure is unimportant.

The structure of a rotation directly influences the opportunity its members have to engage in the iterative process of growth and development that results in fulfilling on-call. The level of that opportunity can be modelled through a combination of individual capability vs organisational friction.

![on-call staffing](oncall-who.png#center "Expected investment level to achieve effective on-call.")

The horizontal axis shows the level of organisational friction to delivering change. Initially this is dominated by communication and co-ordination overheads within and between teams. As the distance from the development team increases (leftwards on the axis), and organisational boundaries accumulate, additional costs in the form of policy, legal and even contractual or financial barriers are added. Often to such an extent that no change at all is possible in fully outsourced environments.

The vertical axis represents the individual capability members of the on-call rotation have to implement change to the system. Encompassing a broad range of factors from their expertise with the production and software development environments, the time available to them and the organisational incentives and motivations that influence where their time is spent.

While the upper right corner might look like utopia the vast majority of effective and fulfilling on-call environments are typically found at various points across the upper-right quadrant. The model acknowledges the reality that every on-call rotation is a balancing of constraints. What the model helps to illustrate is the likely level of investment and types of work that will be required to achieve fulfilling on-call will be for a rotation at any particular point.


## Effective on-call requires leadership support

This model also illustrates the crucial role that leaders of teams and organisations must fulfil in creating an environment that enables effective on-call experiences. In the absence of leadership support, teams and individuals can still drive some gains, but they will come at higher cost than what can be achieved when there is alignment throughout the organisation on the value that on-call can provide.

This is most obviously demonstrated by considering movement on the horizontal axis, where changing which teams the staffing of an on-call rotation is drawn from, or the creation and turn down of entire teams associated with an on-call rotation involve significant organisational management effort and cannot be driven by individuals alone.

Within an on-call rotation, movement upwards on the scale can be incrementally driven by individual and collective improvements to processes and systems even without formal leadership support. However, the size and pace of these increments will be greatly improved by leaders who incentivise and reward time spent learning and improving in the team.


## A framework for effective on-call environments

Returning to the first diagram, there is a notable absence of any structure to support the development of fulfilling on-call practices in the lower-right quadrant. Well established frameworks for project and program management, incident response and general day to day task execution easily come to mind when looking at the other three quadrants. For on-call, there's plenty of individual practices and specific actions recommended, but nothing that draws it all together to help teams provide structure in this important area.

The next few posts will look at how individual practices and specific actions, both those commonly understood today and some that are little talked about, can be combined together to create an effective on-call environment. Guiding teams of many different shapes and sizes to
These two models provide the foundation of a framework to fill that gap which coming posts will explore further by looking at specific practices and actions teams and organisations can take to improve their on-call environment.

What mental models do you use to think about on-call? Are they similar or different to what I've described above?

There's no right or wrong answers here, but having a clear understanding of how we each think about on-call is what leads to productive discussions that deliver learning and help translate experience and recommendations into practical actions that are relevant and useful in our specific situation.
