---
title: GPG Key Transition
author: Matt Brown
type: post
date: 2014-08-17T02:45:17+00:00
aliases: /blog/2014/08/17/gpg-key-transition/
categories:
  - General

---
Firstly, thanks to all who responded to my previous rant. It turns out exactly what I wanted does exist in the form of a ID-000 format smartcard combined with a USB reader. Perfect. No idea why I couldn&#8217;t find that on my own prior to ranting, but very happy to have found it now.

Secondly, now that I&#8217;ve got my keys and management practices in order, it is time to begin transitioning to my new key.

[Click this link to find the properly signed, full transition statement.][1]

I&#8217;m not going to paste the full statement into this post, but my new key is:

<pre>pub   4096R/A48F065A 2014-07-27 [expires: 2016-07-26]
      Key fingerprint = DBB7 64A1 797D 2E21 C799  3CD7 A628 CB5F A48F 065A
uid                  Matthew Brown &lt;matt @mattb.net.nz&gt;
uid                  Matthew Brown &lt;mattb @debian.org&gt;
sub   4096R/1937883F 2014-07-27 [expires: 2016-07-26]
</pre>

If you signed my old key, I&#8217;d very much appreciate a signature on my new key, details and instructions in the [transition statement][1]. I&#8217;m happy to reciprocate if you have a similarly signed transition statement to present.

 [1]: http://www.mattb.net.nz/pgp/key-transition-2014-08-17.txt

## Comments

### Comment by aL on 2014-08-20 01:31:48 +1200
I looked at the web of the ID-000 format smartcard, but couldnt figure out how it works

Are you supposed to hold on your house a key generator (id0) that can generate usb sticks for your everyday use&#8230; or&#8230; Im too interested

Thanks

### Comment by Matt Brown on 2014-08-20 15:31:29 +1200
<a href="http://www.cryptoshop.com/open-pgp-smartcard-v2-id-000.html" rel="nofollow ugc">http://www.cryptoshop.com/open-pgp-smartcard-v2-id-000.html</a>  
<a href="http://www.cryptoshop.com/gemalto-idbridge-k50.html" rel="nofollow ugc">http://www.cryptoshop.com/gemalto-idbridge-k50.html</a>

are the two components I purchased. Snap out the ID-000 format card, insert it into the USB reader, put the case on, voila. you&#8217;re done.

### Comment by Steve on 2014-08-22 13:38:15 +1200
Are you aware of any shops selling the cards & reader (ideally the K50/USB Shell Token v3 rather than the K30/USB Shell Token v2) with non-exorbitant shipping to the US?

### Comment by Matt Brown on 2014-08-22 13:40:23 +1200
I&#8217;ve never looked into shipping to the US sorry. Cryptoshop linked in the previous comment is actually the only place I&#8217;ve seen this combo sold myself. They have both the K30 and the K50.