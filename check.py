#!/usr/bin/env python

import subprocess
from fn1 import log

o = open("names.txt","r")
for NAMES in o:
	log("output", NAMES, "name of person", "stuff")






