#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:31:27 2018

@author: aleksandr
"""

def factorial(n):
    if n == 0:
        print("argument = 0")
        return(1)
    else:        
        a = factorial(n-1)
#        print(a)
#        return(a)
        b = a*n
        print(b)
        return(b)

factorial(4)
