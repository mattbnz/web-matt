---
title: Under the cover of the Kindle 3
type: post
date: 2010-12-07T00:52:50+00:00
aliases: /blog/2010/12/07/under-the-cover-of-the-kindle-3/
categories:
  - Linux
recommended: true

---
For my birthday back in October, my [wonderful wife][1] gave me a [Kindle 3][2] from Amazon. I&#8217;d been considering other e-book readers for quite some time, but I had mostly ignored the Kindle due to the lack of EPUB support and a general dislike of Amazon&#8217;s DRM enforcement. In the end, the superior hardware and ecosystem of the Kindle overpowered those concerns and overall I&#8217;m very pleased with the purchase. The screen is amazing, literally just like reading off a piece of paper and the selection of books is OK. I&#8217;ve been buying almost all my books from Amazon to date since it&#8217;s so easy (the Whispernet is amazingly quick!) but it&#8217;s not terribly difficult to get EPUBs from elsewhere onto the device after a quick run through Calibre to turn them into a MOBI file, so I keep telling myself I&#8217;ve still got some flexibility.

Almost as much fun as reading on the device has been learning about how it works. The [Mobile Read forums][3] have lots of step by step posts on how to do specific tasks like replacing the screensaver image, but they don&#8217;t give much background detail on how the Kindle is actually operating which is what really interests me. Luckily among all the step by step posts I also found a &#8220;usbnetwork&#8221; package which also adds an SSH server to the Kindle,Â so after installing that and then SSHing in to my Kindle I&#8217;ve been poking around.

Under the cover the Kindle reveals a fairly standard Linux installation. While the hardware and IO devices are obviously unique, compared to something like an Android phone, the Kindle is refreshingly &#8220;normal&#8221;.

**Hardware**

  * ï»¿Freescale MX35 ARMv6 based CPU with Java specific instruction support.
  * 256MB RAM
  * 4GB of internal flash presented as an SDHC device with four partitions. A ~700MB root partition, a ~30MB /var/local partition, another roughly 30MB kernel partition and then the rest (~3.1G) as the writeable &#8220;user&#8221; partition where your books and other content are stored. The root and /var/local partitions are ext3! (not jffs or some other more traditional flash based file system) while the user partition is vfat for easy use with Windows, etc.
  * The board is code-named &#8216;luigi&#8217; and there are lots of references to &#8216;mario&#8217; and &#8216;fiona&#8217; scattered around the device, and even in some URLs on Amazon&#8217;s website. Someone was obviously a Super Mario fan.
  * The wireless chipset is Atheros based using the ar6000 drivers.
  * The WAN (3G) modem presents itself as a USB serial device and is controlled via a custom daemon named &#8216;wand&#8217; which uses the standard Linux pppd package to establish IP connections over a private APN Amazon (provided by Vodafone here in Ireland).
  * The EInk display shows up as some special files under `/proc` rather than as a device. With a bit of digging I found some simple constants that when written to the proc files cause the screen to display the standard boot/progress/upgrading images. I haven&#8217;t deciphered how to make more complex updates to the display yet.

**Software**

  * The kernel is based on Linux 2.6.26, with a bunch of hardware specific patches and drivers from [lab126.com][4], an Amazon subsidiary who appear to be responsible for much of the low-level driver and device development.
  * Lots of familiar open source projects are present, e.g. syslog-ng, DBus, busybox, pppd, wpa_supplicant, gstreamer, pango, openssl and the list goes on. You can download all the sources from Amazon&#8217;s website. I haven&#8217;t spent any time to see what if anything has been modified.
  * There were a few unexpected finds as well such as GDB and powertop! No doubt useful for the developers, but highly unlikely to actually be used on a shipping Kindle.
  * Boot-up is controlled by a set of sysv style init scripts which setup the filesystems and then start a handful of daemons to look after the low-level subsystems (network, power, sound) as well as the standard syslog and cron daemons you&#8217;d expect to see on any Linux box.
  * Once the basic system is up and running the init scripts kick off the &#8220;framework&#8221; which lives under `/opt/amazon/ebook` and consists of lots of Java classes. The system uses the cvm Java environment from Sun/Oracle which is specialised for embedded low-memory devices like this. The framework appears to take over most of the co-ordination, management and interaction tasks once it has started up.

The application/framework code is heavily obfuscated apparently using the [Allatori Java Obfuscator][5]. The [jrename][6] and [jd-gui][7] utilities have proven very handy in helping to untangle the puzzle, although they still only leave you with a pile of Java source code with mostly single letter alphabetic variable and class names! I&#8217;ve been using IntelliJ&#8217;s support for refactoring/renaming Java code to slowly work through it (thanks in large part to error/log messages and string constants found through the code which can&#8217;t be obfuscated easily and help to explain what is going on), and I&#8217;m slowly beginning to piece together how the book reading functionality works. I&#8217;ll maybe write more on this in a future post.

In one of my initial tweets about the Kindle I mentioned that it seemed to be regularly uploading syslog data to Amazon based on some `sendlogs` scripts I&#8217;d noticed and a few syslog lines containing GPS co-ordinates that had been pasted on the Mobile Read forums. I can&#8217;t find any trace of GPS co-ordinates in any syslog messages I&#8217;ve seen on my device, but there is definitely information about the cell sites that my Kindle can see, the books that I&#8217;m opening and where I&#8217;m up to in them:
`<br />
101206:235431 wand[2515]: I dtp:diag: t=4cfd77b7,MCC MNC=272 01,Channel=10762,Band=WCDMA I IMT 2000,Cell ID=1362209,LAC=3021,RAC=1<br />
,Network Time=0000/00/00 00.00.00,Local Time Offset=Not provided,Selection Mode=Automatic,Test Mode=0,Bars=4,Roaming=1,RSSI=-88,Tx<br />
 Power=6,System Mode=WCDMA,Data Service Mode=HSDPA,Service Status=Service,Reg Status=Success,Call Status=Conversation,MM Attach St<br />
ate=Attach accept,MM LU State=LU update,GMM Attach State=Attach accept,GMM State=Registered,GMM RAU State=Not available,PDP State=<br />
Active,Network Mode=CS PS separate attach mode,PMM Mode=Connected,SIM Status=Valid; PIN okay; R3,MM Attach Error=No error,MM LU Er<br />
ror=No error,GMM Attach Error=No error,GMM RAU Error=Not available,PDP Rej Reason=No error,Active/Monitored Sets=0;39;-11 1;180;-1<br />
5,RSCP=-111,DRX=64,HSDPA Status=Active,HSDPA Indication=HSDPA HSUPA unsupp,Neighbor Cells=,Best 6 Cells=,Pathloss=,MFRM=,EGPRS Ind<br />
ication=,HPLMN=,RPLMN=272;01 ,FPLMN=234;33  234;30  234;20  272;05 ,n=1:</p>
<p>101206:235758 cvm[3426]: I Reader:BOOK INFO:book asin=B003IWZZ3Y,file size=233168,file last mod date=2010-11-27 19.18.22 +0000,con<br />
tent type=ebook,length=MobiPosition_ 465747,access=2010-12-06 09.44.32 +0000,last read position=MobiPosition_ 464387,isEncrypted=f<br />
alse,isSample=false,isNew=false,isTTSMetdataPresent=false,isTTSMetadataAllowed=true,fileExtn=azw:</p>
<p>101206:233416 udhcpc[5639]: Offer from server xxx.xxx.2.254 received<br />
101206:233416 udhcpc[5639]: Sending select for xxx.xxx.2.10...<br />
`

Interestingly you can see from the last two lines, that Amazon has taken some care to preserve privacy by not including the full IP address given to the device by my local Wifi network, so in light of that I find it interesting that they decided not to obfuscate the Cell and Book IDs in those respective log messages too. Seems rather inconsistent.

As to how and when these logs are sent to Amazon, the picture is a little bit murky. Every 15 minutes `tinyrot` runs out of cron and rotates `/var/log/messages` if it is greater than 256k in size. Rotated logs are stored into `/var/local/log` under filenames like `messages_00000044_20101207000006.gz` and alongside the log files are a set of state files named `nexttosendfile`, `messages_oldest`, `messages_youngest`. Something regularly sweeps through this directory to update the state and remove the old logs (after sending them up to Amazon I assume). I suspect that something is buried in the Java application code mentioned above.

On the whole the Kindle is a fascinating piece of technology. It delivers a wonderful reading experience on top of a familiar Linux system and is going to provide me with many more hours of entertainment as I unpack all the tricks and techniques that have gone into this device. I would recommended it as a present for geeks everywhere.

 [1]: http://www.sweetsnstitches.com/
 [2]: http://www.amazon.com/Kindle-Wireless-Reading-Display-Generation/dp/B003FSUDM4
 [3]: http://www.mobileread.com/forums/forumdisplay.php?f=140
 [4]: http://www.lab126.com
 [5]: http://www.allatori.com/
 [6]: http://adq.livejournal.com/107572.html
 [7]: http://java.decompiler.free.fr/

## Comments

### Comment by Srini Ramakrishnan on 2010-12-07 13:16:23 +1200
Thanks for the very interesting look under the covers Matt, looking forward to your next set of discoveries.

### Comment by Heiko on 2010-12-07 20:40:27 +1200
Dave Jones has a nice video about the real inner workings of the Kindle 3: <a href="http://www.youtube.com/watch?v=lD-wPmowR-Y" rel="nofollow ugc">http://www.youtube.com/watch?v=lD-wPmowR-Y</a>

### Comment by pietro on 2010-12-07 22:30:46 +1200
Thanks for sharing. Did you try to play with iptable or tcpdump to see what kind of information
is sent to amazon ? Or to block the flow ? I would be interested in the hw, but I&#8217;m horrified
by the idea that my reading habits, location and other info will be uploaded to amazon for
marketing purposes. In fact, if I buy one of these, I would almost exclusively use it with
free ebooks available on the net and avoid a vendor lock-in with amazon.

Can you use it as a terminal ? I heard that browsing the web is pretty horrible, but I&#8217;m wondering
if you can run arbitrary applications alongside the java framework and transform the kindle in a
very simple terminal to read email&#8230;

thanks again !

### Comment by anonymous on 2010-12-08 13:11:39 +1200
The reason the progress in your books is sent back is because the Kindle saves your place on Amazon&#8217;s servers to synchronize multiple devices. This feature allows you to switch between your Kindle, the Kindle Android App and Kindle for PC (and all the other Kindle programs) and pick up right where you left off. This is very useful when you want to just read a few pages of your book on your phone while standing in line somewhere. There is an option to disable this.