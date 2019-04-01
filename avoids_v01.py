#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 23:10:02 2019

@author: aleksandr
"""

def avoids(word, forbidden):
    
    for letter in word:
        
        if letter in forbidden:
            
            print(word)
            
#            return False
        
#        return True
    
avoids(open('words.txt'), 'a')
