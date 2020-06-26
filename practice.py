#!/usr/bin/env python
import sys
import time
import smtplib
from fn1 import log
from email.message import EmailMessage

# alert fn

def alert(to, subject, message_body):
	log("INFO", "this is the message i want to send", "Trying to send email alert notification through prod", "n")
	
	msg = EmailMessage()      	#create a new email message
	msg.set_content(message_body)	#set contents of email
	me == blah@gmail.com		#sender email address
	you == blah2@gmail.com		#recipient's email address
	msg['Subject'] = 'this is the subject'
	msg['From'] = me
	msg['To'] = you
		
	print(msg)
	try:
		smtp_server=smtplib.SMTP('localhost')
		smtp_server.send_message(msg)
		#mail stuff here
	except:
		log("WARN", "script host", "Email alert notif failed", "n")
		log("INFO", "script host", "Trying to send email alert again", "n")
		try:
			print(x)
			#more mail stuff
		except:	
			log("ERROR", "script host", "Email alert notif not sent", "n")
		else:
			log("INFO", "script host", "Email notif sent succesfully", "n")
	else:
		log("INFO", "script host", "Email notif sent successfully", "n")

#alert("hi","hi","hi")
	

  
# logger function

#def logger1(dt, l, h, m, f):
#       print(dt+"|"+l+"|"+h+"|"+m, file=open(f, "a"))

# print("Added to file!")

#def logger():
#	dt=sys.argv[1]
#        p=sys.argv[2]
#        l=sys.argv[3]
#        h=sys.argv[4]
#        m=sys.argv[5]
        
#	with open(f, "w") as file:
#	print(dt+"|"+l+"|"+h+"|"+m, f=open(p, 'a'))

#def logger(f, l, h, m):
#	dt=datetime.now()
#o = open(sys.argv[2],'a')

#print("Adding file...")
#print(sys.argv[1]+"|"+sys.argv[3]+"|"+sys.argv[4]+"|"+sys.argv[5], file=o


def logger(f, l, h, m):
	dt=time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')
	o = open(f,'a')
	p = open(l,'r')
	l = p.read()
	print(dt+"|"+l+"|"+h+"|"+m, file=o)


logger("hello",'file_of_names',"name","is")

