KindleRSSDaily
===

File framework and templates are from 'dailykindle' https://github.com/pelletier/dailykindle.
 -Modified it to support Chinese.
 -Updated the out-dated API of feedparder


How to use:
 -1. Put your user-name and password in a file outside the repo in two lines.
 -2. Specify the location of that file in send.py, let p = open('FILE_LOCATION','r')
 -3. Put the rss resource in sources.txt line by line.
 -4. Config send.py to send the mobi file to your kindle email
 -5. Config the contab on the server to run send.py every day.



