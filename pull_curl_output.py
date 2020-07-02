#!/usr/bin/env python

import subprocess

#result=subprocess.check_output(['./redirect.sh'])
#print(result)

result=subprocess.Popen("./redirect1.sh", cwd="/Users/edenchou/documents/comp_projects/shell_to_python/scripts")
result.wait()					#waits till shell script is finished executing before moving on
o=open("/Users/edenchou/documents/comp_projects/shell_to_python/scripts/output","r")
print(o.read())


#print(output_result)
#convert=str(result,'utf-8')
#convert=convert.readlines()
#convert=convert[:-1]						#remove newline
#o=open(convert, 'r')
#l=o.read()
#print("contents of the file:")
#print(l)

