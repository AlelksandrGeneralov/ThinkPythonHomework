#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:29:31 2019

@author: aleksandr
"""

fin = open('words.txt')
t = []

for line in fin:
    t.append(fin.readline())

print(t)