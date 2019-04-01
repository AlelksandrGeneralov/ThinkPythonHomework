#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:02:42 2019

@author: aleksandr
"""

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
        words.insert(1, 'a')
        words.insert(3, 'b')

print(words)