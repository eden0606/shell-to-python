#!/usr/bin/env python
import subprocess, os
import shlex #allows the use of parameters

#print("This is my introduction:")

#subprocess.Popen(['./callee.sh', "Eden"])

#subprocess.Popen(['./callee.sh', &name 'Eden'])

#subprocess.call([". \"./callee.sh\";", "&name"])

add_result=subprocess.call(shlex.split('./add_fn.sh 3 4'))
print(add_result)
print("this is the sum: " + str(add_result))

print(".......................")

print_file_result=subprocess.check_output(['./print_file.sh', "output", "testing whitespace capabilities"])
convert=str(print_file_result,'utf-8')
convert=convert[:-1]
#remove newline

o=open(convert, 'r')
l=o.read()
print("contents of the file:")
print(l)

#subprocess.call(['./callee.sh'])
#exec(open("./callee.sh").read())



