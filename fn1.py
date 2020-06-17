#!/usr/bin/env python

# logger function

def logger():
	print(str(sys.argv[1])+"|"+str(sys.argv[3])+"|"+str(sys.argv[4])+"|"+str(sys.argv[5]), file=open(str(sys.argv[2]), "a"))


print("Added to file!")
logger()
