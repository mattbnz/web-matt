---
title: InternetNZ and DNS Censorship
date: 2025-03-31 12:55:28+13:00
draft: true
categories:
- Technology
buttondown:
  id: cdab79e1-6e0c-4e58-ad62-ab34e5a758bd
---

InternetNZ is the incorporated society that runs the .nz ccTLD. I've been a member for many years. I also had the privilege of serving on the review panel that advised on changes to the rules governing how .nz is operated at the last major review several years ago. It's an organisation I feel some ownership in, and care about the future of.

The .nz ccTLD is well regarded internationally. The model of using profits earned from domain registration fees to fund projects and programmes that benefit the growth and development of the Internet community in New Zealand has served both the organisation and the country well over the past decades. Perhaps due to this, the reality has long been that most kiwis don't know the organisation exists and the number of members has remained stubbornly low.

But in the last few months, the membership has [dramatically changed](https://billbennett.co.nz/internetnz-disrupted/).

A "free speech" group encouraged their members to join and oppose a proposed new constitution for the organisation, ostensibly over concerns it would lead to censorship of registrations in the .nz zone. That's been followed by a counter-surge of sign-ups from others who distrust and dislike the aims and assumed motives of the new members.

**I think the concerns are misplaced - they relate to matters better dealt with in the separate .nz rules. The new constitution is not perfect, but I'm in favour of it overall and I hope to see it pass at this evening's SGM.**

But while the concerns with the constitution and motivations behind them may be questionable, there is still a worthwhile conversation to reconcile the diverse viewpoints around what InternetNZ should be as an organisation and how .nz should be operated that needs to continue.

Engaging with the conversation in recent weeks has helped confirm my opinion regarding the policies that should be applied to .nz, but unexpectedly has also led me to question whether InternetNZ's current form is going to be fit for purpose in future.


## Background Context

Broadly speaking, the dominating issue is what role the DNS (and more specifically the .nz ccTLD) and related organisations such as InternetNZ should play in addressing bad things that happen on the Internet (in NZ).

On one end of the spectrum is an argument that there is a duty to actively minimise harm, including efforts to prevent negative outcomes and advocacy to improve and layer additional protections. The other end of the spectrum would argue that DNS is a foundational technology that should be operated with only the minimum restrictions and policies necessary, and specifically that using DNS to address harm is treating the symptom rather than the underlying issue.

Historically and affirmed in the recent review, InternetNZ's policies for management of .nz have contained a "no concern for use" statement, placing the organisation towards the latter "hands off" end of the spectrum. At the same time, the organisation has always used the profits from that work to engage in sponsorship and execution of projects which naturally seem to tend and pull more towards the former "minimise harm" end.

The current discussions are just the latest iteration in a long, ongoing debate over how to manage the inherent tension arising from the dual roles that the structure of organisation presents.

Relevant events from the last several years to be aware of in terms of adding context to this include:

* The [introduction of the emergency and exceptional circumstances clause](https://internetnz.nz/news-and-articles/ensuring-nz-can-respond-emergencies-and-crises/) allowing domains to be suspended following the Christchurch mosque shootings in 2019.
* The [.nz rules review](https://internetnz.nz/nz-domains/nz-rules/nz-policy-review/nz-policy-review-archive/#review2019) that affirmed the "no concern for use" policy as well as the emergency clause while also recommending establishment of a trusted notifier regime to replace it.
* The [2021 council resignations](https://businessdesk.co.nz/article/technology/pakeha-old-boys-club-maori-women-quit-internetnz), [subsequent systemic racism review](https://internetnz.nz/systemic-racism-review/) and the resulting commitment to become a Te Tiriti focused organisation.
* A proposal (not adopted) in the [conflicted domain resolution policy consultation](https://internetnz.nz/nz-domains/conflicted-domain-names-policy-review/) that included consideration of the purpose of use in resolution of conflicted domains.
* A general sense that society is unhappy with the level of harm on the Internet and wants "something" done, with domain names and DNS being the most visible and obvious offender. [This article](https://www.nzherald.co.nz/business/auckland-transport-warns-about-pretend-parking-site-registered-with-internetnz-using-fake-details/42KK6ZH545AU7F5DBPG3UNW63Q/) from last week is representative in tone.

It's a lot to stay on top of, even for someone deeply interested in the space and issues like me!


## The role of DNS

I'm generally in favour of a harm minimisation approach towards the Internet (and life in general), but DNS is not an effective layer for such efforts to be focused on.

Those in power should manipulate DNS as a rare, last resort for addressing bad things happening in the world. Cancelling a DNS registration is an incredibly blunt action with high risk of collateral damage, and is usually ineffective anyway as the content simply moves to a different name. Attempting to prevent a registration before there is any evidence of bad use is an equally bad idea - the cost/benefit of cancelling an existing name where there is evidence of bad use rarely add up, and when the evidence of such use is only probabilistic or predicted based on limited information the outcomes will be even worse.

The absence or immaturity of layers of protection elsewhere in society means that we can expect to see DNS names being used for bad and harmful purposes. That is painful, but we need to take it as evidence of the gaps elsewhere, not in DNS itself. In the same way that we don't look to the companies office or the phonebook provider as the primary action to prevent or stop the harm when bad actors utilise their services.

That's not to argue that a DNS registry should take a completely hands-off approach. In order for the other layers of society to be able to operate effectively there needs to be transparency and accountability into who is responsible for a DNS name, and the ability to act on suspension or cancellation orders from lawfully authorised bodies.

### Current .nz policy

The current .nz policies demonstrate a balance: The "no concern for use" principle is clearly stated and the only allowances against it are the exceptional circumstances clause, or in response to a lawful court order. In parallel the policies require accurate registration details to be provided, and allow cancellation of registrations if and when those details cannot be verified.

The policy choice to focus enforcement actions on an objectively fraudulent action (providing false registration details) rather than a subjective determination of use works well. The only tweak I would like to see, is a more formal "trusted notifier" regime established to cover all cases where registrations can be cancelled. This would replace the exceptional circumstances policy and leave all subjective decisions to the legal system.

### Room for operational improvements

Although the policy situation for .nz is close to optimal, there is still room for significant improvement in how the existing policies are applied and operated with respect to the verification and enforcement of accurate registration details.

More responsibility for ensuring registrant details are valid should be pushed back to the registrars and options for registrants to explicitly link their registrations to identifiers such as an NZBN or RealMe identity as a way of scaling validation and coverage of provably accurate registration details need to be actively explored.

Outside of those changes, any other attempts to change .nz policy to more actively consider the use or purpose of a registration do not seem justified and should be strongly resisted.


## If not DNS, where?

That begs the question of where and how we should focus on minimising harm from the Internet if the DNS ecosystem is not the right place to do it.

The answer is everywhere and through our normal everyday laws, culture and ways of being. The Internet is no longer some special or unique place distinct from everyday or real life - it's just another way, perhaps the most common way for many of us, in which we interact, communicate and share life together.

### Implications for the future of InternetNZ

That is both an amazing success, but also a sobering reality check: attempting to sustain an organisation of InternetNZ's current and historical nature, where charitable good purposes are pursued and funded out of the profits of the DNS registry may no longer be feasible or wise.

The country is diverse, and the DNS registry has to be responsive and fair to that diversity of views and perspectives. It's a hard task, but it's achievable when you recognise that DNS is not the level at which to solve societal issues. It's not luck or accident that this is where .nz policy has landed. It's a justifiable position, but it can be hard to accept given it leaves a lot of problems for other parts of society to solve.

The ever present tension between the needs of the registry policies and the desires to use those profits to further purposes on the charitable side of the organisation has historically been managable because the Internet was new and novel enough that there was sufficient common ground in promoting its adoption and use in general that the organisation could unite around that in spite of different perspectives around the more contentious topics.

Today, with the Internet just another aspect of life in general, I'm not optimistic that sufficient common purposes to unite around can be found, or that the efforts to do so will be worth the effort - particularly if they put the current .nz rules and policies at risk.

## Food for thought

**What would we lose if InternetNZ downscoped its role to running the registry, cut domain registration fees to eliminate the profits that currently fund the charitable efforts and created space for other organisations to take up that work without the inherent tension of also operating the registry?**

It's clear there would be a loss - most notably in the short term of the funding grants InternetNZ distributes to various community projects, and more broadly to the policy and advocacy work the organisation undertakes.

On the positive side it would clarify the organisation's role and allow for clearer and more focused discussions around .nz rules and policy, with lower domain registration fees for the community as a pleasing side effect.

What's unclear is whether the short-term loss would translate into a long-term net negative for NZ overall, or whether other groups would take up the policy and advocacy roles in a more effective and sustainable manner than InternetNZ can achieve while trying to satisfy all stakeholders. The tension inherent between InternetNZ's dual roles has been managed to date, and the organisation has achieved many good things, but that's not say the approach is obviously the best or only one that should be considered.

Perhaps the expectation that other organisations could fill that gap, and be more effective than InternetNZ without the funding that the domain registration revenue provides is wishful thinking, but as I've pondered over these topics in the last few weeks I've found it harder and harder to convince myself that the current model is easily justifiable going forward.

I think it's worth exploring the question more - maybe there are better answers or solutions that I haven't thought of yet.
