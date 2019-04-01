#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:38:55 2018

@author: aleksandr
"""

word = 'y'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

move_index = 25
    
index_in_word = 0
 
while index_in_word < len(word):
    
    letter_in_word = word[index_in_word] 
    
#    print(letter_in_word)
    
    index_in_alphabet = 0
    
    while index_in_alphabet < len(alphabet):
        
        letter_in_alphabet = alphabet[index_in_alphabet]
        
#        print(letter_in_alphabet)
        
        if letter_in_word == letter_in_alphabet:
            
            new_index_in_alphabet = (index_in_alphabet + move_index) % len(alphabet)
            
            result = alphabet[new_index_in_alphabet]
            
            print(result)
            
        index_in_alphabet = index_in_alphabet + 1

    index_in_word = index_in_word + 1
