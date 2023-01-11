---
title: GPG Key Management Rant
author: Matt Brown
type: post
date: 2014-07-12T00:17:58+00:00
aliases: /blog/2014/07/12/gpg-key-management-rant/
categories:
  - Debian
  - Linux
  - WLUG / LinuxNZ

---
2014 and it&#8217;s still annoyingly hard to find a reasonable GPG key management system for personal use&#8230; All I want is to keep the key material isolated from any Internet connected host, without requiring me to jump through major inconvenience every time I want to use the key.

An HSM/Smartcard of some sort is an obvious choice, but they all suck in their own ways:
* FSFE smartcard &#8211; it&#8217;s a smartcard, requires a reader, which are generally not particular portable compared to a USB stick.
* Yubikey Neo &#8211; restricted to 2048 bits, doesn&#8217;t allow imports of primary keys (only subkeys), so you either generate on device and have no backup, or maintain some off-device primary key with only subkeys on the Neo, negating the main benefits of it in the first place.
* Smartcard HSM &#8211; similar problems to the Neo, plus not really supported by GPG well (needs 2.0 with specific supporting module version requirements).
* Cryptostick &#8211; made by some Germans, sounds potentially great, but perpetually out of stock.

Which leaves basically only the &#8220;roll your own&#8221; dm-crypt+LUKS usb stick approach. It obviously works well, and is what I currently use, but it&#8217;s a bunch of effort to maintain, particularly if you decide, as I have, that the master key material can never touch a machine with a network connection. The implication is that you now need to keep an airgapped machine around, and maintain a set of subkeys that are OK for use on network connected machines to avoid going mad playing sneakernet for every package upload.

The ideal device would be a USB form factor, supporting import of 4096 bit keys, across all GPG capabilities, but with all crypto ops happening on-device, so the key material never leaves the stick once imported. Ideally also cheap enough (e.g. ~100ish currency units) that I can acquire two for redundancy.

As far as I can tell, such a device does not exist on this planet. It&#8217;s almost enough to make a man give up on Debian and go live a life of peace and solitude with the remaining 99.9% of the world who don&#8217;t know or care about this overly complicated mess of encryption we&#8217;ve wrought for ourselves.

end rant.

## Comments

### Comment by Andy Cater on 2014-07-12 21:13:09 +1200
You could do worse than contact Daniel Silverstone and whoever else made the Simtec entropy key. They should have the smarts to make a GPG enforcing key better than the Yubikey and it will come in tamper resistant housing 🙂

### Comment by William Hay on 2014-07-13 01:12:22 +1200
The reader I use with my FSFE card(<a href="http://www.amazon.com/SCM-SCR3500-Smart-Card-Reader/dp/B00434WQVU" rel="nofollow ugc">http://www.amazon.com/SCM-SCR3500-Smart-Card-Reader/dp/B00434WQVU</a>) folds down to about the same size as a USB stick. The card itself fits in my wallet.

### Comment by Ryan Nowakowski on 2014-07-13 01:55:57 +1200
The old Black Dog server on a USB stick might be an option.

### Comment by Anonymous on 2014-07-13 02:59:20 +1200
What about the FSFE smartcard and a small-form-factor USB card reader?

### Comment by Red7 on 2014-07-13 04:31:59 +1200
You can cut the FSFE smart card down to ID-000 size, and then use a USB-dongle sized reader, as described here: <a href="https://www.gnupg.org/howtos/card-howto/en/ch02s02.html#id251938" rel="nofollow ugc">https://www.gnupg.org/howtos/card-howto/en/ch02s02.html#id251938</a>

### Comment by Simon Josefsson on 2014-07-13 21:52:32 +1200
The Neo supports primary key on card, as far as I know. Still 2048 bits though. I find it convenient to use sub keys on a neo: I would not want to revoke my master key if I lose my neo, but could easily revoke a set of sub keys if I lose my neo, and generate a new set of sub keys on another neo. This way I don&#8217;t disrupt the web of trust.

/Simon

### Comment by G on 2014-07-14 03:15:30 +1200
What you describe as ideal exists: it&#8217;s an OpenPGP v2 smartcard (like the FSFE
card) [1] with an ID000 form factor USB smartcard reader [2]. It works as
advertised in Debian.

[1]: <a href="http://shop.kernelconcepts.de/product_info.php?cPath=1_26&#038;products_id=42" rel="nofollow ugc">http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=42</a>
[2]: <a href="http://shop.kernelconcepts.de/product_info.php?cPath=1_26&#038;products_id=119" rel="nofollow ugc">http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=119</a>

### Comment by Tobias on 2014-07-14 23:31:02 +1200
Did you look at Gnuk (<a href="http://www.fsij.org/category/gnuk.html" rel="nofollow ugc">http://www.fsij.org/category/gnuk.html</a>) and FST-01 (<a href="http://www.seeedstudio.com/wiki/FST-01" rel="nofollow ugc">http://www.seeedstudio.com/wiki/FST-01</a>) &#8211; This is compatible with GnuPG, but AFAIK it only support 2048-Bit keys &#8211; the reasoning being that longer keys make operations on the hardware awfully slow.

Or you could combine the Gemalto USB Shell Token (<a href="http://shop.kernelconcepts.de/product_info.php?cPath=1_26&#038;products_id=119" rel="nofollow ugc">http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=119</a>) with a OpenPGP smart card (e.g. <a href="http://shop.kernelconcepts.de/product_info.php?cPath=1_26&#038;products_id=42" rel="nofollow ugc">http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=42</a> or the FSFE card, cut to size) and get another nice, small, hopefully tamper-resistant token.

### Comment by G on 2014-07-18 21:18:06 +1200
I&#8217;m confused. I left a comment a few days ago which showed up on the site right away &#8212; now it&#8217;s gone. I hope you saw it; if it got lost, I&#8217;ll be happy to post it again.

### Comment by Chris Boot on 2014-07-23 06:27:13 +1200
I use an OpenPGP smart card in a USB-stick sized reader (Gemalto ID Bridge K50). It works great with GnuPG 2.x and well enough with 1.x, and supports 4096-bit keys in all three slots simultaneously. It&#8217;s essentially the FSFE smartcard with a SIM cutout in a small reader.

You can usually get the smart cards from <a href="http://shop.kernelconcepts.de/product_info.php?cPath=1_26&#038;products_id=42" rel="nofollow ugc">http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=42</a>. I source the readers myself from elsewhere in the UK (<a href="http://smartware2u.com/products/73-gemalto-id-bridge-k50-shell-token.aspx" rel="nofollow ugc">http://smartware2u.com/products/73-gemalto-id-bridge-k50-shell-token.aspx</a>).

HTH,
Chris

### Comment by Corsac on 2014-07-28 01:24:21 +1200
Use an OpenPGP card with SIM breakout (<a href="http://shop.kernelconcepts.de/product_info.php?cPath=1_26&#038;products_id=42" rel="nofollow ugc">http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=42</a>) and add an USB token (<a href="http://shop.kernelconcepts.de/product_info.php?cPath=1_26&#038;products_id=119" rel="nofollow ugc">http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=119</a>)

### Comment by Matt Brown on 2014-08-11 01:14:42 +1200
Thanks for all the comments, and apologies for moderation delays&#8230; WordPress apparently stopped emailing me when comments are held for moderation so I only found the queue today 🙁

In any case, the OpenPGP smart card in ID000 form factor with a USB reader was also suggested to me on G+, and fits the bill perfectly. I&#8217;ve got the working nicely now.

Rant resolved 😉
