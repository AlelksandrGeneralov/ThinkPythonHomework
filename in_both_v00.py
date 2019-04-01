#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 21:16:38 2018

@author: aleksandr
"""

def in_both(w1, w2):
    for letter in w1:
        if letter in w2:
            print(letter)
            
in_both('qwerty', 'aqsdfgh')