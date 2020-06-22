#!/usr/bin/env python
import time

# log function

def log(f, l, h, m):
        dt=time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')
        o = open(f,'a')
        print(dt+"|"+l+"|"+h+"|"+m, file=o)


