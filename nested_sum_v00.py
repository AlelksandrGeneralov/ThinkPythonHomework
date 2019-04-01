#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:27:35 2019

@author: aleksandr
"""

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 10]

def nested_sum(l):
    
    total = 0
    
    for i in l:
        if isinstance(i, list): #check if i is list 
            total = total + nested_sum(i)   
        else:
            total = total + i
    return(total)
        
print(nested_sum(l))