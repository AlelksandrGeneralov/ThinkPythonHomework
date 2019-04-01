#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:21:56 2019

@author: aleksandr
"""

l = list('kot')
l1 = list('tok')

def is_annagrams(t, t1):
    t.sort()
    t1.sort()
    if t == t1:
        return(True)
    return(False)
    
    
print(is_annagrams(l, l1))