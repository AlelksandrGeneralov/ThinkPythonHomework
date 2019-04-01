#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 22:01:52 2018

@author: aleksandr
"""

def is_reverse(w1, w2):
    if len(w1) != len(w2):
        print(len(w1), 'do not match to ', len(w2))
    else:
        i = 0
        j = len(w2) - 1
    
        while j > 0:
            print(w1[i])
            print(w2[j])
#            if w1[i] == w2[j]:
#                print(True)
            i = i + 1
            j = j - 1
#                
#            print(False)
        
    
is_reverse('qwerty', 'ytrewa')