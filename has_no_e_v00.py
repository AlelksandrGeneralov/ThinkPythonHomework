#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:30:12 2018

@author: aleksandr
"""

fin = open('words.txt')

i = 0
j = 0

for line in fin:
    
    i = i + 1
    
    for letter in line:
        
        if letter == 'e':
        
            j = j + 1
            
#            pass
        
#            print(letter)

print((i-j)*100/i)
    
#print('total amount of words', i)


        
        