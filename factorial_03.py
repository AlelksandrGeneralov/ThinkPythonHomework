#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:24:12 2018

@author: aleksandr
"""

def fact(n):
    f = 1
    
    for i in range(1, n + 1):
        f = f*i
        
    return(f)
        
x = 4

result = fact(x)

print(result)