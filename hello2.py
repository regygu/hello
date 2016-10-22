#!/usr/bin/env python3

import sys

arglist = sys.argv

def lenght_of_arglist(arglist):
    return len(arglist)


if lenght_of_arglist(arglist) == 1:
    print("Hello World")

else:      
    print("Hello " + arglist[1])
