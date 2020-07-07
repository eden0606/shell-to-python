#!/usr/bin/env python
import time

# log function

def log(f, l, h, m):
	dt=time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')
	o = open(f,'a')
#	p = open(l,'r')
#	l = p.read()
	print(dt+"|"+l+"|"+h+"|"+m, file=o)
# log("names",'file_of_names', "is", "test")


