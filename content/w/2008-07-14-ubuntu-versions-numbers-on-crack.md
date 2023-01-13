---
title: Ubuntu versions numbers on crack

date: 2008-07-13T15:56:25+00:00
aliases: /blog/2008/07/14/ubuntu-versions-numbers-on-crack/
categories:
  - Debian
  - Linux
  - WLUG / LinuxNZ

---
On hardy after the latest round of updates:

`<br />
matt@krypton:~$ dpkg -s flashplugin-nonfree | grep Version<br />
Version: 10.0.1.218+10.0.0.525ubuntu1~hardy1+really9.0.124.0ubuntu2<br />
` 

Granted this package is in hardy-backports not hardy proper, but still, what on earth?!?!

## Comments

### Comment by Philipp Kern on 2008-07-14 05:05:38 +1200
Well, it&#8217;s documented in the changelog on \`https://edge.launchpad.net/ubuntu/+source/flashplugin-nonfree&#8217;. Ubuntu more or less refrains from using epochs unilaterally[0]. This upload was done to undo a bad backport to hardy, i.e. an old version (9.0.124.0ubuntu2) was uploaded to supersede one with a higher version number (10.0.1.218+10.0.0.525ubuntu1~hardy1).

I&#8217;m not entirely sure about the first part (10.0.1.218+10.0.0.525ubuntu1). Looking at the changelog 10.0.1.218 was in the archives before and 10.0.0.525 denotes a new &#8220;upstream beta&#8221; somehow. Might be a screw-up of Adobe, I don&#8217;t know.

[0] The main problem is that the version need to be kept with the epoch for all times until Debian also uses that very epoch. Until then the package needs to be merged manually instead of being synced from Debian.

### Comment by Markus Thielmann on 2008-07-14 07:47:16 +1200
Adobes Flash 10 Beta 2 (10.0.0.525) has a lower release number than Beta 1 (10.0.1.218).

### Comment by ScottK on 2008-07-14 09:25:34 +1200
Phillip is right. That was the least impact way to undo a bad backport and give users a way to upgrade out of the mess. Ugly but effective. Better I hadn&#8217;t approved the backport in the first place, but to late for that.

[WORDPRESS HASHCASH] The poster sent us &#8216;0 which is not a hashcash value.