#!/usr/bin/env python

import subprocess

#result=subprocess.check_output(['./redirect.sh'])
#print(result)




result=subprocess.Popen(['./redirect.sh'])
result.wait()					#waits till shell script is finished executing before moving on
o=open("output","r")
print(o.read())


#print(output_result)
#convert=str(result,'utf-8')
#convert=convert.readlines()
#convert=convert[:-1]						#remove newline
#o=open(convert, 'r')
#l=o.read()
#print("contents of the file:")
#print(l)

