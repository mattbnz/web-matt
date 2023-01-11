---
title: GPG Keysigning Update
type: post
date: 2009-06-26T00:56:03+00:00
aliases: /blog/2009/06/26/gpg-keysigning-update/
categories:
  - Debian
  - WLUG / LinuxNZ

---
From the better late than never category&#8230; I finally got around to signing keys from the LCA2006 key signing party, the verification sheet from which has travelled with me from NZ to Dublin and then sat on my desk for a few years. I inevitably lost a few of my notes and verifications along the way, so if you were still expecting a signature from me and didn&#8217;t get one let me know!

The main hold up for me has been that my previous key signing system, a home grown script, was overly complex and involved me sending an encrypted token to each UID that I waited to receive back before issuing the signature. Lots of work for me, and much hassle for those whose keys I am signing. I&#8217;ve reverted back to the more standard method of signing and encrypting the signature to each UID and then throwing my copy of the signature away. Unless the recipient controls the UID and can decrypt the message, the signature will never be released to the world. 

I&#8217;ve adopted [pius][1] as my new signing tool of choice, with a few extra patches to help me maintain my database of signature details and the corresponding verification pages at <http://www.mattb.net.nz/pgp/signatures> which are linked from the Policy URL packet of each signature I make. I guess I&#8217;ll tidy up the patches over the next few days and see if there is any interest in getting them merged.

 [1]: http://www.phildev.net/pius/

## Comments

### Comment by foo on 2009-06-26 16:58:30 +1200
pius isn&#8217;t in Debian, could you package it? Also, why not just use caff from signing-party?

### Comment by matt on 2009-06-26 20:27:04 +1200
I can certainly investigate packaging pius for Debian. 

Caff is perl, and I don&#8217;t really do perl, pius is Python, and I enjoy Python, so it was an easy choice for me.