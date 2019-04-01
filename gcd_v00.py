#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:56:37 2018

@author: aleksandr
"""

def gcd(a, b):
    r = a%b
    print("r = ", r)
    if r == 0:
        print("gsd = ", b)
    else:
        gcd(b, r)
        
gcd(150, 15)
    
    