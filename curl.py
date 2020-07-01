#!/usr/bin/env python

import os, sys, subprocess
from threading import Timer

#result=subprocess.Popen(["curl", "--head", "https://www.google.com"], timeout=20, stdout=subprocess.PIPE)
#(out,err)=result.communicate()
#out=str(out,'utf-8')
#out=out[:-1]

#out= os.popen("curl --silent --show-error -i -H 'X-Requested-By: Eden' -X GET -k 'https://edenchou.com' | grep 'FOODIE' | awk -F '=' {'print $1'}").read()

kill = lambda process: process.kill()

cmd="curl --silent --show-error -i -H 'X-Requested-By: Eden' -X GET -k 'https://edenchou.com' | grep 'FOODIE' | awk -F '=' {'print $1'}"
out=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

my_timer = Timer(20, kill, [out])

try:
	my_timer.start()
	out=out.communicate()[0]
	out=str(out,'utf-8')
	out=out[:-1]
	print(out)
finally:
	my_timer.cancel()

#out=subprocess.Popen(["curl", "--silent", "--show-error", "-i", "-H", "X-Requested-By: Eden", "-X", "GET", "-k", "https://edenchou.com"], stdout=subprocess.PIPE)
#to perform multiple piped commands must use shell=True or use one subprocesses for each pipe

# | grep 'FOODIE' | awk -F '=' {'print $1'}"]).read()







