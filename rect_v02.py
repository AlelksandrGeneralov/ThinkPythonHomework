#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:34:25 2019

@author: aleksandr
"""

import graphics as gr

window =   gr.GraphWin('wondow', 700, 700)

def rect(A, B):
    gr.Line(A, B).draw(window)
    
rect((100, 100),(200, 200))