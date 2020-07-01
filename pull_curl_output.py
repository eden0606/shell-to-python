#!/usr/bin/env python

import subprocess

subprocess.Popen(['./redirect.sh'])
o=open("output","rb")

print(str(o.read(), 'utf-8'))


#print(output_result)
#convert=str(output_result,'utf-8')
#convert=convert.readlines()
#convert=convert[:-1]						#remove newline
#o=open(convert, 'r')
#l=o.read()
#print("contents of the file:")
#print(l)

