KindleRSSDaily
===
Author Shuai Lu (sl988@cornell.edu)

Modified by xg1990#gmail.com


KindleRSSDaily helps you convert RSS resources to mobi and deliver it to your kindle through email evryday.

Code framework and templates are from 'dailykindle' https://github.com/pelletier/dailykindle.
kindlegen is the deafault conversion tool of amazon for kindle (V2.9).


Dependencies:
-----

linux  packages:  postfix, wget, imagemagick

python packages:  feedparser, jinja2



How to use:
---------

0. Setup your postfix and make sure `mail` command works.
1. Put the rss resource in sources.txt line by line.
2. Config send.py to send the mobi file to your kindle email
3. Config the contab on the server to run dailyRSS.sh every day.


