#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:52:06 2019

@author: aleksandr
"""

l = [1, 2, 3, 1, 2, 1, 4, 5, 5, 7, 6, 8, 8, 8]

def remove_duplicates(t):
    t.sort()
    t1 = []
    print(t)
    i = 0
    imax = len(t)-2
    
    while i <= imax:
        if t[i] != t[i+1]:
            t1.append(t[i])
            print(t1)
        i += 1
    t1.append(t[-1])
    return(t1)
    
print(remove_duplicates(l))
