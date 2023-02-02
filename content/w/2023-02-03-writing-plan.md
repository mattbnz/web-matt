---
title: "2023 Writing Plan"
date: 2023-02-03T10:07:21+13:00
recommended: true
contactsidebar: true

categories:
  - General
---

To achieve my [goal]({{< relref "2023-goals.md" >}}) of publishing one high-quality piece of writing per week this year, I've put together a draft writing plan and a few organisational notes.

**Please let me know what you think - what's missing? what would you like to read more/less of from me?**

I aim for each piece of writing to generate discussion, inspire further writing, and raise my visibility and profile with potential customers and peers. Some of the writing will be opinion, but I expect a majority of it will take a "learning by teaching" approach - aiming to explain and present useful information to the reader while helping me learn more!

## Topic Backlog

The majority of my writing is going to fit into 4 series, allowing me to plan out a set of posts and narrative rather than having to come up with something novel to write about every week. To start with for Feb, my aim is to get an initial post in each series out the door. Long-term, it's likely that the order of posts will reflect my work focus (e.g. if I'm spending a few weeks deep-diving into a particular product idea then expect more writing on that), but I will try and maintain some variety across the different series as well.

This backlog will be maintained as a living page at https://www.mattb.nz/w/queue.


**Thoughts on SRE**

This series of posts will be pitched primarily at potential consulting customers who want to understand how I approach the development and operations of distributed software systems. Initial topics to cover include:

 * What is SRE? My philosophy on how it relates to DevOps, Platform Engineering and various other "hot" terms.
 * How SRE scales up and down in size.
 * My approach to managing oncall responsibilities, toil and operational work.
 * How to grow an SRE team, including the common futility of SRE "transformations".
 * Learning from incidents, postmortems, incident response, etc.

**Business plan drafts**

I have an ever-growing list of potential software opportunities and products which I think would be fun to build, but which generally don't ever leave my head due to lack of time to develop the idea, or being unable to convince myself that there's a viable business case or market for it.

I'd like to start sharing some very rudimentary business plan sketches for some of these ideas as a way of getting some feedback on my assessment of their potential. Whether that's confirmation that it's not worth pursuing, an expression of interest in the product, or potential partnership/collaboration opportunities - anything is better than the idea just sitting in my head.

Initial ideas include:
 * Business oriented Mastodon hosting.
 * PDF E-signing - e.g. A Docusign competitor, but with a local twist through RealMe or drivers license validation.
 * A framework to enable simple, performant per-tenant at-rest encryption for SaaS products - stop the data leaks.

**Product development updates**

For any product ideas that show merit and develop into a project, and particularly for the existing [product ideas I've already committed to exploring]({{< relref "2023-goals.md#product-development" >}}), I plan to document my product investigation and market research findings as a way of structuring and driving my learning in the space.

To start with this will involve:
  * A series of explanatory posts diving into how NZ's electricity system works with a particular focus on how operational data that will be critical to managing a more dynamic grid flows (or doesn't flow!) today, and what opportunities or needs exist for generating, managing or distributing data that might be solvable with a software system I could build.
  * A series of product reviews and deep dives into existing farm management software and platforms in use by NZ farmers today, looking at the functionality they provide, how they integrate and generally testing the anecdotal feedback I have to date that they're clunky, hard to use and not well integrated.
  * For [co2mon.nz](https://co2mon.nz/) the focus will be less on market research and more on exploring potential distribution channels (e.g. direct advertising vs partnership with air conditioning suppliers) and pricing models (e.g. buy vs rent).

**Debugging walk-throughs**

Being able to debug and fix a system that you're not intimately familiar with is valuable skill and something that I've always enjoyed, but it's also a skill that I observe many engineers are uncomfortable with. There's a set of techniques and processes that I've honed and developed over the years for doing this which I think make the task of debugging an unfamiliar system more approachable.

The idea, is that each post will take a problem or situation I've encountered, from the initial symptom or problem report and walk through the process of how to narrow down and identify the trigger or root cause of the behaviour. Along the way, discussing techniques used, their pros and cons. In addition to learning about the process of debugging itself, the aim is to illustrate lessons that can be applied when designing and building software systems that facilitate and improve our experiences in the operational stage of a systems lifecycle where debugging takes place.

**Miscellaneous topics**

In addition the regular series above, stand-alone posts on the other topics may include:

  * The pros/cons I see of bootstrapping a business vs taking VC or other funding.
  * Thoughts on remote work and hiring staff.
  * AI - a confessional on how I didn't think it would progress in my lifetime, but maybe I was wrong.
  * Reflections on 15 years at Google and thoughts on subsequent events since my departure.
  * AWS vs GCP. Fight! Or with less click-bait, a level-headed comparison of the pros/cons I see in each platform.


## Logistics

### Discussion and comments

A large part of my motivation for writing regularly is to seek feedback and generate discussion on these topics. Typically this is done by including comment functionality within the website itself. I've decided not to do this - on-site commenting creates extra infrastructure to maintain, and limits the visibility and breadth of discussion to existing readers and followers.

To provide opportunities for comment and feedback I plan to share and post notification and summarised snippets of selected posts to various social media platforms. Links to these social media posts will be added to each piece of writing to provide a path for readers to engage and discuss further while enabling the discussion and visibility of the post to grow and extend beyond my direct followers and subscribers.

My current thinking is that I'll distribute via the following platforms:

 * Mastodon [@matt@mastodon.nz](https://mastodon.nz/@mattb) - every post.
 * Twitter [@xleem](https://www.twitter.com/xleem) - selected posts. I'm trying to reduce Twitter usage in favour of Mastodon, but there's no denying that it's still where a significant number of people and discussions are happening.
 * [LinkedIn](https://www.linkedin.com/in/mattbrown/) - probably primarily for posts in the business plan series, and notable milestones in the product development process.

In all cases, my aim will be to post a short teaser or summary paragraph that poses an question or relays an interesting fact to give some immediate value and signal to readers as to whether they want to click through rather than simply spamming links into the feed.

### Feedback

In addition to social media discussion I also plan to add a direct feedback path, particularly for readers who don't have time or inclination to participate in written discussion, by providing a simple thumbs up/thumbs down feedback widget to the bottom of each post, including those delivered via RSS and email.

### Organisation

To enable subscription to subsets of my writing (particularly for places like Planet Debian, etc where the more business focused content is likely to be off-topic), I plan to place each post into a set of categories:

* Business
* Technology
* General

In addition to the categories, I'll also use more free-form tags to group writing with linked themes or that falls within one of the series described above.
