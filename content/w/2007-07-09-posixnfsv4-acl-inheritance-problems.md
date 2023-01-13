---
title: POSIX/NFSv4 ACL Inheritance Problems

date: 2007-07-08T16:23:49+00:00
aliases: /blog/2007/07/09/posixnfsv4-acl-inheritance-problems/
categories:
  - Linux
  - WLUG / LinuxNZ

---
I (as root) have a directory hierarchy that I want a particular group to always have write access to. The files and folders inside the hierarchy are owned and manipulated by a wide variety of diffrent users. 

Essentially I want to delegate &#8216;root&#8217; access for a portion of the filesystem to a particular group. 

My first attempt at implementing this was to use the standard [POSIX ACLs][1] that are available for almost every filesystem Linux supports.

I recursively set an ACL on the top-level directory to give the group write access to all files and directories that currently exist and then I recursively set a default ACL to give the group write access on all the directories. This default ACL should be inherited by any new files that are created ensuring that the group keeps write access to everything. 

Problem solved? Unfortunately not.

The intricacies of complying with POSIX means that ACLs are implemented as an ACL plus a mask. To gain access to a particular file or directory the user or group must match an appropriate ACL granting the access and the mask for that file or directory must also allow the requested permission to be granted.

When you add an ACL to a file or directory, the &#8216;group&#8217; bits of the standard Unix permissions magically switch from controlling group access to controlling the mask portion of the ACL, effectively providing an upper bound on the permissions that an ACL entry can grant. This prevents legacy POSIX applications that do not understand ACLs from unintentionally granting excessive permissions &#8211; arguably a good thing.

Unfortunately this also makes it very hard to preserve the ACL granting write access to the &#8216;root&#8217; group which I legitimately intended to have in place on this portion of the filesystem. 

Newly created files under the hierarchy generally inherit the ACL as intended, as most applications attempt to create files with as many permissions as possible, leaving it up to the umask to remove undesired permissions.

However any file that is copied into the hierarchy without the &#8216;group&#8217; write bit set, or any file that has the &#8216;group&#8217; write bit removed via chmod will actually remove the write bit from the ACL mask invalidating the ACL and leaving me back at square one!

After a bit of Googling I thought that [NFSv4 ACLs][2] might be the answer to this problem, as they are marketed as &#8220;very similar to Windows ACLs&#8221; and I&#8217;m sure that I vaugely recall Windows being able to properly inherit ACLs from parent directories. Unfortunately after downloading the NFSv4 ACL patches and trying all the various mount options I cannot find any combination that will offer the functionality I need. The implementation conforms to POSIX, so it still has a mask parameter and the same problems as the standard POSIX ACLs. The only benefit from using NFSv4 ACLs that I can see is that you have more permissions to grant.

So once again, I&#8217;m back to square one. I&#8217;m hoping that there is some fundamental point that I&#8217;m missing as this seems like a very common use-case that I would have thought would be well supported. 

If a command-line example is clearer to you look at:  
<http://www.mattb.net.nz/blog/dump/acl-inheritance-problems.txt>

My current solution is to run a cronjob every X minutes to recursively &#8216;chmod -R g+w /dir&#8217;, however that&#8217;s far from optimal as it exposes all sorts of race conditions and just seems ugly!

Any suggestions or solutions will be gratefully received.

 [1]: http://www.suse.de/~agruen/acl/linux-acls/online/
 [2]: http://www.suse.de/~agruen/nfs4acl/