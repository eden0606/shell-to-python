#!/usr/bin/env python

import sys
o = open('outfile1','a')

print("Adding file...")
print(sys.argv[1], file=o)

#o.close()
