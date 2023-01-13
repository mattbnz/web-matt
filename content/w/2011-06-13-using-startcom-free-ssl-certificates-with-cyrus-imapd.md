---
title: Using StartCom Free SSL certificates with Cyrus imapd

date: 2011-06-12T21:12:13+00:00
aliases: /blog/2011/06/13/using-startcom-free-ssl-certificates-with-cyrus-imapd/
categories:
  - Linux

---
A stumbled across [Start Com][1] a few months ago, an Israeli company that run a Certificate Authority (CA) called [StartSSL][2] with a root certificate in all the modern browsers and operating systems. Best of all they don&#8217;t participate in the cartel run by the rest of the SSL certificate industry and offer domain validated certificates at the price it costs them to issue them &#8211; nothing.

I had the first opportunity to use their services today when I needed an SSL cert to secure the IMAP server I run for my parents and I was very pleased with the experience. The web interface is a bit weird and you have to jump through some strange hoops, but to save paying more money to the SSL certificate cartel it seemed more than worthwhile.

Like most CAs these days the certificate which signs your server certificate is not the actual root certificate included in your operating system or browser, but an intermediate CA certificate which is in turn signed by the root certificate. This means that you have to ensure that your server includes the intermediate CA certificate alongside the server certificate so the client can validate the entire path back to the root.

Unlike Apache which explicitly allows you to specify a certificate chain file, the openssl methods used by Cyrus 2.2 only seem to recognise a single CA certificate in the file pointed to by `tls_ca_file`. All as not lost however, as the openssl libraries are actually quite smart and will automagically determine which intermediate certs they need to bundle into the handshake if you install them appropriately under /etc/ssl/certs (at least on Debian).

The trick is that you have to install the intermediate CA cert into a file named after the hash of the certificate, like so:  
`<br />
# wget http://www.startssl.com/certs/sub.class1.server.ca.pem -O /etc/ssl/certs/startcom-class1-intermediate.pem<br />
# hash=$(openssl x509 -hash -noout -in /etc/ssl/certs/startcom-class1-intermediate.pem)<br />
# ln -s ./startcom-class1-intermediate.pem /etc/ssl/certs/${hash}.0<br />
# ls -l /etc/ssl/certs/${hash}.0<br />
lrwxrwxrwx 1 root root 34 2011-06-13 07:43 /etc/ssl/certs/ea59305e.0 -> ./startcom-class1-intermediate.pem<br />
` 

Then in `imapd.conf`:  
`<br />
tls_cert_file: /etc/ssl/certs/your-server-cert.pem<br />
tls_key_file: /etc/ssl/private/your-server-key.key<br />
tls_ca_file: /etc/ssl/certs/startcom-ca.pem<br />
` 

Voila. Works everywhere I&#8217;ve tried so far.

Start Com &#8211; Highly Recommended. I&#8217;ll be using them for any future SSL certificate purchases (e.g. EV certs) that I need to make.

 [1]: http://www.startcom.org/
 [2]: https://www.startssl.com/

## Comments

### Comment by Philipp Kern on 2011-06-13 09:32:54 +1200
Please note that revocation actually costs real money.

### Comment by Ben on 2011-06-13 16:15:00 +1200
Also note that the certificates aren&#8217;t &#8220;Free&#8221;â„¢; StartCom retains all rights, etc..

Be sure to read their Certification Policy! (&#8220;Subscribers Obligations&#8221; link on the StartSSL homepage or, this document: http: //www.startssl.com/policy.pdf )

### Comment by Vincent Bernat on 2011-06-13 18:34:50 +1200
The other way to make the intermediate CA work is just to concatenate it to your certificate (first your certificate, then the intermediate CA). You can also concatenate the intermediate CA to the CA (first the CA, then the intermediate CA).

### Comment by matt on 2011-06-13 21:14:22 +1200
Vincent, I&#8217;ve used that technique with other servers, but Cyrus seems to only ever read the first certificate in the file from what I can make out.

### Comment by Dmitrijs Ledkovs on 2011-06-21 18:39:11 +1200
Hmmm&#8230;.. certificate issuing is suspended due to security breach&#8230;..

### Comment by matt on 2011-06-21 19:05:46 +1200
Hmm, that&#8217;s very unfortunate&#8230;