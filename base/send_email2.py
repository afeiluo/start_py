#!/usr/bin/python
import smtplib

SERVER = "your.smtp.server"

FROM = "my@email.com"
TO = ["your@email.com"] 

SUBJECT = "Testing"

TEXT = "This is a test email using Python."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()