#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:37:09 2018

@author: aleksandr
"""

fin = open('words.txt')
#print(fin)

for line in fin:
    
    word = line.strip()
    
    if len(word) > 20:
        
        print(word)



