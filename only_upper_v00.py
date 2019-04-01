#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:06:32 2019

@author: aleksandr
"""

l = ["AA", "b", "Xx"]

def only_upper(l):
    new_l = []
    for a in l:
        if a.isupper():
            new_l.append(a)
    return(new_l)
    
print(only_upper(l))