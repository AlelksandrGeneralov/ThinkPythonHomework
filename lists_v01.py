#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:49:54 2019

@author: aleksandr
"""

l = ["a", "b", "c", "d", "e", "f", "g"]

def capitalize_all(l):
    
    new_l = []
    
    for a in l:
        new_l.append(a.capitalize())
        
    return(new_l)
    
print(capitalize_all(l))
