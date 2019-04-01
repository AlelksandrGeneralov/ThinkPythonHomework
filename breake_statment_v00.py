#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:01:37 2019

@author: aleksandr
"""

for n in range(1, 10):
    for x in range(2, n):
        print(x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a primer')
        
for i in range(1, 1):
    print(True)
else:
    print(False)