#!/usr/bin/env python
  
# logger function

def logger(dt, l, h, m, f):
        print(dt+"|"+l+"|"+h+"|"+m, file=open(f, "a"))


print("Added to file!")
logger("i", "am", "uber", "cool", "file_of_names")


