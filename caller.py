#!/usr/bin/env python
import subprocess, os
import shlex #allows the use of parameters

#print("This is my introduction:")

#subprocess.Popen(['./callee.sh', "Eden"])

#subprocess.Popen(['./callee.sh', &name 'Eden'])

#subprocess.call([". \"./callee.sh\";", "&name"])

#result=subprocess.call(shlex.split('./callee.sh file_of_names testing123'))

result=subprocess.check_output(['./callee.sh', "output", "newtest123"])
convert=str(result,'utf-8')
convert=convert[:-1]
#remove newline

o=open(convert, 'r')
l=o.read()
print("contents of the file:")
print(l)
#print("this is the sum: " + str(result))

#subprocess.call(['./callee.sh'])
#exec(open("./callee.sh").read())



