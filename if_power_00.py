#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:35:40 2018

@author: aleksandr
"""

def if_power(a, b):
    r = a%b
#    power = a/bhttps://www.linuxmint.com/start/tara/
    if r == 0:
        power = a/b
        if a == (b**power):
            print(True)
        else:
            print(False)
    else:
        pass
#        print(False)
        
if_power(8, 2)
        
        
        
        