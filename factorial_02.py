#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:10:12 2018

@author: aleksandr
"""

def fac(n):
    fac = 1
    i = 0
    while i < n:
        i = 1
        fac = fac*i
        print(fac)
    return fac

fac(3)