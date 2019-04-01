#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:39:33 2018

@author: aleksandr
"""

def ack(m, n):
    if m == 0:
        print(ack(n + 1))
    elif m > 0 and n == 0:
        print(ack(m - 1, 1))
    elif m > 0 and n > 0:
        print(ack(m - 1, ack(m, n - 1)))
        
ack(3, 4)