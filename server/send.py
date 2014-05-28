from datetime import timedelta
import os
import dailykindle
import time

email="username@kindle.com"

f = open("sources.txt", "r")
feeds = f.readlines()
f.close()

dailykindle.build(feeds, '../temp/', timedelta(1))
dailykindle.mobi('../temp/daily.opf', '../kindlegen/kindlegen')

date = time.strftime("%Y-%m-%d")

os.system("mv %s %s" %('../temp/daily.mobi', '../temp/daily'+date+'.mobi'))
os.system("mail -a %s -s \"%s\" %s </dev/null" %('../temp/daily'+date+'.mobi','Daily RSS'+ date, email));
