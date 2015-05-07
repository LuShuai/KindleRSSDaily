KindleRSSDaily
===
Author Shuai Lu (sl988@cornell.edu)

KindleRSSDaily helps you convert RSS resources to mobi and deliver it to your kindle through email evryday.


Code framework and templates are from 'dailykindle' https://github.com/pelletier/dailykindle.
kindlegen is the deafault conversion tool of amazon for kindle (V2.9).

1. Modified it to support Chinese.
2. Updated the out-dated API of feedparser


How to use:

1. Put your user-name and password in a file outside the repo in two lines.
2. Specify the location of that file in send.py, let p = open('FILE_LOCATION','r')
3. Put the rss resource in sources.txt line by line.
4. Config send.py to send the mobi file to your kindle email
5. Config the contab on the server to run dailyRSS.sh every day.



