#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:55:13 2018

@author: aleksandr
"""

def fac(n):
    space = ' ' * (4 * n)
    print (space, 'fac', n)
    
    if n == 0:
        print(space, 'returning 1')
        return(1)
    else:
        a = fac(n-1)
        b = a*n
        print (space, 'returning',b)
        return(b)
        
fac(5)
    
    