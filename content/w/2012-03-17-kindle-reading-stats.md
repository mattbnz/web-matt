---
title: Kindle Reading Stats
date: 2012-03-17T23:08:27+00:00
aliases: /blog/2012/03/17/kindle-reading-stats/
categories:
  - General
recommended: true
---
I&#8217;ve [written before][1] about my initial investigations into the Kindle, and I&#8217;ve learnt much more about the software and how it communicates with the Amazon servers since then, but it all requires detailed technical explanation which I can never seem to find the motivation to write down. Extracting reading data out of the system log files is however comparatively simple.

I&#8217;m a big fan of measurement and data so my motivation and goal for the Kindle log files was to see if I could extract some useful information about my Kindle use and reading patterns. In particular, I&#8217;m interested in tracking my pace of reading, and how much time I spend reading over time.

You&#8217;ll recall from the previous post that the Kindle keeps a fairly detailed syslog containing many events, including power state changes, and changes in the &#8220;Booklet&#8221; software system including opening and closing books and position information. You can eyeball any one of those logfiles and understand what is going on fairly quickly, so the analysis scripts are at the core just a set of regexps to extract the relevant lines and a small bit of logic to link them together and calculate time spent in each state/book.

You can find the scripts on Github: https://github.com/mattbnz/kindle-utils

Of course, they&#8217;re not quite that simple. The Kindle doesn&#8217;t seem to have a proper hardware clock (or mine has a broken hardware clock). My Kindle comes back from every reboot thinking it&#8217;s either at the epoch or somewhere in the middle of 2010, the time doesn&#8217;t get corrected until it can find a network connection and ping an Amazon server for an update, so if you have the network disabled it might be many days or weeks of reading before the system time is updated to reality. Once it has a network connection it uses the MCC reported by the 3G modem to infer what timezone it should be in, and switches the system clock to local time. Unfortunately the log entries all look like this:

```
110703:193542 cvm[7908]: I TimezoneService:MCCChanged:mcc=310,old=GB,new=US:
110703:193542 cvm[7908]: I TimezoneService:TimeZoneChange:offset=-25200,zone=America/Los_Angeles,country=US:
110703:193542 cvm[7908]: I LipcService:EventArrived:source=com.lab126.wan,name=localTimeOffsetChanged,arg0=-25200,arg1=1309689302:
110703:193542 cvm[7908]: I TimezoneService:LTOChanged:time=1309689302000,lto=-25200000:
110703:183542 system: I wancontrol:pc:processing "pppstart"
110703:193542 cvm[7908]: I LipcService:EventArrived:source=com.lab126.wan,name=dataStateChanged,arg0=2,arg1=<none>:
110703:183542 cvm[7908]: I ConnectionService:LipcEventArrived:source=com.lab126.cmd,name=intfPropertiesChanged,arg0=</none><none>,arg1=wan:
110703:183542 cvm[7908]: W ConnectionService:UnhandledLipcEvent:event=intfPropertiesChanged:
110703:193542 wifid[2486]: I wmgr:event:handleWpasupNotify(<2>CTRL-EVENT-DISCONNECTED), state=Searching:
110703:113542 wifid[2486]: I spectator:conn-assoc-fail:t=374931.469106, bssid=00:00:00:00:00:00:
110703:113542 wifid[2486]: I sysev:dispatch:code=Conn failed:
110703:183542 cvm[7908]: I LipcService:EventArrived:source=com.lab126.wifid,name=cmConnectionFailed,arg0=Failed to connect to WiFi network,arg1=</none><none>:
</none>
```

Notice how there is no timezone information associated with the date/time information on each line. Worse still the different daemons are logging in at least 3 different timezones/DST offsets all interspersed within the same logfile. Argh!!

So our simple script that just extracts a few regexps and links them together nearly doubles in size to handle the various time and date convolutions that the logs present. Really, the world should just use UTC everywhere. Life would be so much simpler.

The end result is a script that spits out information like:
```
B000FC1PJI: Quicksilver: Read  1 times. Last Finished: Fri Mar 16 18:30:57 2012
 - Tue Feb 21 11:06:24 2012 => Fri Mar 16 18:30:57 2012. Reading time 19 hours, 29 mins (p9 => p914)
...
Read 51 books in total. 9 days, 2 hours, 29 mins of reading time
```

I haven&#8217;t got to the point of actually calculating reading pace yet, but the necessary data is all there and I find the overall reading time stats interesting enough for now.

If you have a jailbroken Kindle, I&#8217;d love for you to have a play and let me know what you think. You&#8217;ll probably find logs going back at least 2-3 weeks still on your Kindle to start with, and you can use the `fetch-logs` script to regularly pull them down to more permanent storage if you desire.

 [1]: http://www.mattb.net.nz/blog/2010/12/07/under-the-cover-of-the-kindle-3/ "Under the cover of the Kindle 3"
