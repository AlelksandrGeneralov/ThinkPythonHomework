#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:59:50 2019

@author: aleksandr
"""

l = [["a", "b"], ["c", "d"], "e"]
new_l = []

def capitalize_all(l):
    new_l = []
    for a in l:
        new_l.append(a.capitalize())    
    return(new_l)
print(capitalize_all(l))



def capitalize_nested(l):    
    for a in l:
        if isinstance(a, list):
            capitalize_nested(a)
        else:
            new_l.append(a.capitalize())
    return(new_l)    
print(capitalize_nested(l))