#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:17:22 2019

@author: aleksandr
"""

def avoids(fin, forbidden):
    
    i = 0   #words counter
    j = 0   #forbidden words counter
    
#    fin = open('words.txt')
    
    for word in fin:
            
        for letter in word:
            
            if letter in forbidden:
                
                print(letter)
                
                j = j + 1
            
        i = i + 1
    
    print('counter of words ', i)
            
    print('counter of words which contained forbidden letters ', j)

avoids(open('words.txt'), 'acefhlo')

