---
title: Linux ignores IPv6 router advertisements when forwarding is enabled
type: post
date: 2011-05-11T23:26:52+00:00
aliases: /blog/2011/05/12/linux-ignores-ipv6-router-advertisements-when-forwarding-is-enabled/
categories:
  - Linux

---
IPv6 adoption is increasing, and along with it come a new set of behaviours and defaults that system administrators and users must learn and become familiar with. I was recently caught out by Linux&#8217;s handling of IPv6 router advertisements (RAs) when forwarding is also enabled on the interface. It took me a while to figure out and searching for obvious terms (such as those in the first half of the title of this post) didn&#8217;t immediately yield useful answers, so here is my attempt to help shed some light on the subject.

By default Linux will ignore IPv6 RAs if the interface is configured to forward traffic. This is in line with [RFC2462][1] which states that a device should be either a Host or a Router. If you&#8217;re forwarding packets you&#8217;re a router and you&#8217;re therefore expected to be sending RAs, not receiving them. This policy does make a certain amount of sense but there are obviously situations where it can be useful to accept RAs and still forward packets over the interface[0]. The confusing part is that the Linux IPv6 stack allows the `accept_ra` sysctl to be set to 1 (enabled) at the same time as the `forwarding` sysctl is set to 1, yet all incoming RAs are ignored with no hint as to why. If you&#8217;re not aware that the default behaviour is to ignore RAs when forwarding is enabled it looks very much like autoconfiguration has simply broken.

The key piece of information is that makes everything as clear as mud is realising that the `forwarding` and `accept_ra` sysctl&#8217;s are not simple boolean enabled/disabled flags like many of their brethren. There are instead three possible values for each, all clearly documented in [sysctl.txt][2], when you take the time to read it. Ironically the documentation states the type of the values as &#8220;BOOLEAN&#8221; even though they&#8217;re not&#8230; at least it helped me to feel better about my hasty assumption that the sysctl&#8217;s were boolean values.

> accept_ra &#8211; BOOLEAN  
> Accept Router Advertisements; autoconfigure using them.
> 
> Possible values are:  
> 0 Do not accept Router Advertisements.  
> 1 Accept Router Advertisements if forwarding is disabled.  
> 2 Overrule forwarding behaviour. Accept Router Advertisements  
> even if forwarding is enabled.
> 
> Functional default: enabled if local forwarding is disabled.  
> disabled if local forwarding is enabled. 

The documentation for `forwarding` is similar, but much longer, so you can refer to the link above to see it.

Conclusion: If you want to autoconfigure IPv6 addresses on an interface that you&#8217;re also forwarding IPv6 traffic over, you need to set `accept_ra` to 2.

No doubt there are more IPv6 quirks and defaults like this waiting to trap me in the future 🙂

[0] Arguably you really don&#8217;t want to be autoconfiguring addresses on your router ever, but that&#8217;s a philosophical debate that isn&#8217;t really relevant to this post.

 [1]: http://tools.ietf.org/html/rfc2462
 [2]: http://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt

## Comments

### Comment by Giovanni on 2011-05-15 08:01:03 +1200
Having autoconfigured addresses on a routing machine isn&#8217;t that absurd in my opinioni. Here we have wireless devices that can be moved across different subnets, while offering the same address pool to their clients: they configure statically their wireless interface, but have to request (or autoassign) dinamically the address towards the wired network (then OSPF is used to inform the central router of their position).