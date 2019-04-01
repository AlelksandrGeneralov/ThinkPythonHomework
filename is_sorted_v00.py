#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:25:19 2019

@author: aleksandr
"""

l = [3, 2, 1]

def is_sorted(t):  
    i = len(t)-1
    while i >= 0:
        if t[i] > t[i-1]:
            return(True)
            i = i-1
        else:
            return(False)
        
        

    
print(is_sorted(l))
