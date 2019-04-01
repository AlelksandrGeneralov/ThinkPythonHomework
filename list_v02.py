#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:18:41 2019

@author: aleksandr
"""

l = [1, 2, 3, 4, 5, 6, 1]

#print(l[1] + l[0])

new_l = []

def func(l):
    i = 0
    for a in l:
        if i == 0:
            new_l.append(l[i])
            i = i+1
        else:
            new_l.append(new_l[i-1] + l[i])
            i = i+1
    return(new_l)
    
print(func(l))
        
        
        