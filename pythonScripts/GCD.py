#!/usr/bin/env python

import sys

def GCD(a,b):
    while b:
        a, b = b, a % b
    return a

print(GCD(100,200))

    
