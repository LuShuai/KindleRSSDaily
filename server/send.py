from datetime import timedelta
import smtplib
import os
import dailykindle
import sendgrid
import time


f = open("sources.txt", "r")
feeds = f.readlines()
f.close()

dailykindle.build(feeds, '../temp/', timedelta(1))
dailykindle.mobi('../temp/daily.opf', '../kindlegen/kindlegen')

date = time.strftime("%m/%d/%Y")
message = sendgrid.Mail()
sg = sendgrid.SendGridClient('ludaxia', 'lssnqbbA1990726')
message = sendgrid.Mail()
message.add_to('sl988@kindle.com')
message.set_subject('Daily RSS'+ date)
message.add_attachment("DailyRSS"+date+".mobi",'../temp/daily.mobi')
message.set_from('sl988@cornell.edu')
message.set_text('RSS DAILY ' + date)
status, msg = sg.send(message)
print '[' + str(status) + ']' + msg




