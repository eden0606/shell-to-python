#!/usr/bin/env python
import subprocess, os
import shlex #allows the use of parameters

print("This is my introduction:")

subprocess.Popen(['./callee.sh', "Eden"])

#subprocess.Popen(['./callee.sh', &name 'Eden'])

#subprocess.call([". \"./callee.sh\";", "&name"])

#subprocess.call(shlex.split('./callee.sh name "Eden"'))
#subprocess.call(['./callee.sh'])
#exec(open("./callee.sh").read())



