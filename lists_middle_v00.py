#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:01:37 2019

@author: aleksandr
"""

l = [1, 2, 3, 4, 5, 6, 1]
new_l = []

def lists_middle(l):
    i = len(l)
    new_l = l[1:i-1]
    return(new_l)
    
print(lists_middle(l))
    