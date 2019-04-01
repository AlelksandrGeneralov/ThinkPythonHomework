#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:03:56 2019

@author: aleksandr
"""

def delete_head(t):
    del(t[0])
    return(t)
    
l = ['a', 'b', 'c']
print(delete_head(l))