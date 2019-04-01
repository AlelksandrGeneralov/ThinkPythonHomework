#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:36:07 2019

@author: aleksandr
"""

l = [1, 2, 3, 4, 1, 2]

def is_duplicates(t):
    ts = t[:]
    ts.sort()

    i = 0
    imax = len(ts)-2
    
    while i <= imax:
        if ts[i] == ts[i+1]:
            return(True)
            print(i)
        i += 1
    return(False)

print(is_duplicates(l))


    

