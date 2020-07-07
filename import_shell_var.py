#!/usr/bin/env python

import os
import pprint 					# pretty printer -- so data can be used for an interpreter
import shlex
import subprocess

command = shlex.split("env -i bash -c 'source export_shell_var.sh'")
proc = subprocess.Popen(command, stdout = subprocess.PIPE)
for line in proc.stdout:
	(key, _, value) = line.partition("=")
	os.environ[key] = value
	
proc.communicate()

pprint.pprint(dict(os.environ))

print(os.environ.get('dir'))







