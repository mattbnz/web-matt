---
title: GPG Key Signing Policy of Matt Brown
date: 2014-08-17
---

To communicate with me using GPG please use the key below.

    pub   rsa4096 2014-07-27 [SC] [expires: 2026-09-30]
          DBB764A1797D2E21C7993CD7A628CB5FA48F065A
    uid           Matthew Brown <matt@mattb.net.nz>
    uid           Matthew Brown <mattb@debian.org>
    sub   rsa4096 2014-07-27 [E] [expires: 2026-09-30]

You can import it from [here (ascii armored)](/keys/A48F065A.asc), or any good keyserver.

Prior to August 2014, I used 59B2D9A0 as my primary key, however I am now transitioning away from that key, so please don't use it for anything anymore.

[17 Aug 2014: Key Transition Statement](/keys/key-transition-2014-08-17.txt)

## Signed Keys
See the complete list of keys I have signed [here](/pgp/signatures/).

## Key Signing
I have a fairly strict key signing policy that I adhere to. This policy is described in the details below. As a part of this policy I maintain a registry of the keys I have signed and the verification steps I took before signing on this website. A link to the appropriate entry in this registry is appended to each UID I sign as a policy URL.

Despite debate over the value of the different signature types (see RFC 2440 section 5.2.1), I perceive them to be beneficial, if only for my own personal use. The following table lists the minimum requirements that I will require to be satisified before I will sign a UID. This table is a guide and you should refer to the policy URL on an individual signature for the definitive description of the steps I took before signing that particular UID.

|Type|Description|My Policy|
|-|-|-|
|0x10|Generic Certification|I hope to only rarely use this type of signature. One example of a case where I would use it would be if a keyholder has satisified by casual signature requirements, but there is a problem with their key (such as an inspecific uid) that leads me to believe their key is not so useful for verifying their identity.|
|0x11|Persona Certification|I do not intend to use this signature type. In my opinion it breaks the point of signing keys, I will trust you less if you make signatures of this type.|
|0x12|Casual Certification|To sign your key with a casual signature, I will need to have met you in person and sighted at least one form of government issued photo identification. For each uid that you want me to sign, I will need to verify that the email address is active and accessible by the keyholder.|
|0x13|Positive Certification|To sign your key with a postive signature, you will need to satisfy my requirements for a casual signature AND additionally, have been personally known to me for at least one year.|

## Why are you sending me email?
If we recently met and exchanged key details with a view to signing each others keys then it is highly likely that you will receive an encrypted email from me. Within that email (when decrypted) will be the signature for your key. You will receive one email to each uid listed on your key. The purpose of these encrypted emails is to ensure that you (the holder of the key I signed) are in control of the email addresses associated with the signed uids.

My apologies if you receive this email to multiple uids, it is necessary to decrypt and import the signature from each one individually.

## Comments
If you have comments about my key signing policy, please feel free to contact me using the details on the front page of my site.

## Revision History
 * **17 Aug 2014** - Updated to reflect transition to A48F065A.
 * **23 Dec 2007** - Updated fingerprint and public key (59B2D9A0) to reflect the addition of a new signing subkey (36933EA3) as the previous subkey (4054AB08) is about to expire.
 * **23 Oct 2006** - Removed debian@mattb.net.nz uid and added mattb@debian.org uid. I'm now a real Debian Developer!
 * **19 Mar 2006** - Removed matt@medialab.co.nz uid.
 * **4 Jan 2006** - Updated fingerprint and public key (59B2D9A0) to reflect the addition of a new signing subkey (4054AB08) to be used for email and other signing tasks in less secure environments.
