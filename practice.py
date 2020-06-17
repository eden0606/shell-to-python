#!/usr/bin/env python
import sys
  
# logger function

#def logger1(dt, l, h, m, f):
#       print(dt+"|"+l+"|"+h+"|"+m, file=open(f, "a"))

# print("Added to file!")

#def logger():
#	dt=sys.argv[1]
#        p=sys.argv[2]
#        l=sys.argv[3]
#        h=sys.argv[4]
#        m=sys.argv[5]
        
#	with open(f, "w") as file:
#	print(dt+"|"+l+"|"+h+"|"+m, f=open(p, 'a'))

#logger()

o = open(sys.argv[2],'a')

print("Adding file...")
print(sys.argv[1]+"|"+sys.argv[3]+"|"+sys.argv[4]+"|"+sys.argv[5], file=o)

 

