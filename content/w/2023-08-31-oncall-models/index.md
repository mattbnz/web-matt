---
title: "Mental models of on-call"
description: Establishing common ground for a practical discussion of how to realise the opportunity on-call presents.
date: 2023-08-23T15:37:24+13:00
draft: true

card_image: oncall-opportunity.jpg

categories:
  - Technology
---
The [mental models](https://en.wikipedia.org/wiki/Mental_model) in our heads shape every discussion. Understanding how they align or differ between participants in a conversation is an important aspect of effective communication. This is particularly relevant for topics such as on-call where a wide range of different experiences lead to strongly held opinions.

This post steps back from high-level discussion of the opportunity on-call offers to focus on describing two key mental models I use to think about on-call and the roles and responsibilities of the different people involved.


 ## What is on-call?

Beyond the obvious concept of on-call being responsible for fixing something when it breaks, I find that looking at where on-call sits in the broader landscape of work required to develop and operate a software system provides a more useful model for understanding what it involves.

![on-call work model](oncall-what.png#center "The landscape of software work, with apologies for the ugly diagram.")

 On the horizontal axis is the time window within which the work must be completed, from months on the left to minutes on the right. On the vertical axis is the number of people directly involved in completing the unit of work, from a single individual at the bottom up to the entire company at the top.

 On-call occupies a space roughly consistent with the bottom-right quadrant, bounded by days on the left, and multiple people above. Requiring an urgent (hours to minutes) response, but within the scope that one or two people can resolve.

This framing of on-call shows why responsiveness is key, but also explains why [on-call is inevitable]({{% relref "2023-08-16-oncall-opportunity.md#on-call-is-inevitable" %}}) (there will always be work falling in this quadrant regardless of whether you want it to or not) and why [on-call and incident response require distinct planning and preparation]({{% relref "2023-08-16-oncall-opportunity.md#the-narrow-scope-of-existing-tools" %}}) (they handle different scales of event and response).


## Who should be on-call?

In an ideal world everyone developing software would benefit from the opportunity for growth and development that on-call provides, but a simplistic "you build it, you run it" answer is not sufficient because realisation of the opportunity requires an effective on-call environment.

Creating an effective on-call environment requires balancing many constraints. A key indicator that an effective balance is being achieved is the [presence of growth]({{% relref "2023-08-16-oncall-opportunity.md#checking-the-direction-of-travel" %}}), which comes with [learning through iteration]({{% relref "2023-08-16-oncall-opportunity.md#growth-through-iteration" %}}).

Faster iterations mean more growth opportunities. The structure and staffing of an on-call rotation play a significant role in determining the likely cost or level of investment required to complete each iteration of learning.

![on-call staffing](oncall-who.png#center "Expected cost/investment required to achieve iterative growth.")

The staffing of an on-call rotation can be drawn as a shape on this chart that reflects where the individuals are located and their capacity for iteration. Distance from the development team slows iteration speed due to organisational friction. Missing skill sets, limited time and conflicting incentives limit individual capacity to participate in iterative learning.

The goal is to be near to the top right of this scale, while recognising that there are forces constantly pushing away from the ideal in the top-right corner that constrain what is realistically achievable.

The location and the shape of on-call rotation that provides the best outcome for any particular situation will vary based on the unique constraints involved. There is no easy or universally optimal answer to how an on-call rotation should be staffed. Effective and fulfilling on-call environments can be found in much of the upper-right quadrant.

The model helps to understand what type and level of investment will likely be required to achieve that, or to improve from the current position regardless of where that is located.


## Leadership support is key

Effective on-call environments require committed leadership.

This is most obvious when looking reducing organisational friction. Changing the teams staffing for an on-call rotation is drawn from, or the creation and turn down of entire teams associated with an on-call rotation involve significant organisational management effort and cannot be driven by individuals alone.

Within an on-call rotation, individual and collective efforts can drive incremental improvement in the capacity to iterate even without formal leadership support. However, the size and pace of these increments will be limited. Supportive leadership that provides time and opportunity for this work as well as overall support for growth and learning will significantly improve the pace at which iteration capacity increases.

Improving from high iteration cost to a lower iteration cost environment provides the clearest illustrations of the need for committed leadership, but the requirement does not stop once an effective on-call environment has been achieved. Continued leadership and committent is required to sustain the environment in the face of the constant forces pushing away from the desired state.


## A framework for effective on-call environments

Thinking about the poor reputation of on-call through the lens of these models leads me to the conclusion that what is often missing is guidance for leaders and teams wanting to make practical improvements upwards or rightwards in their on-call environment. Recommendations for individual practices and specific actions that can improve on-call can be found, but not as a comprehensive or complete structure.

Well established frameworks for project and program management, incident response and general day to day task execution easily come to mind when looking at the other three quadrants in the first model, but I'm not aware of anything similar in the on-call space.

Over the next few posts, I plan to use these models to describe a framework for on-call that I've found adds this structure and as a result, enables the opportunity of on-call to be realised in a team.

To get the most out of that discussion, I challenge you to think about what mental models you use to describe on-call? Are they similar or different to what I've described above?

There's no right or wrong answers here, but having a clear understanding of how we each think about on-call is the foundation for the ability to translate diverse experiences and recommendations into practical actions that are relevant and useful in our specific situation.