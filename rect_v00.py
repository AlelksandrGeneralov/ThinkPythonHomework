#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:34:25 2019

@author: aleksandr
"""

import graphics as gr

window =   gr.GraphWin('wondow', 300, 300)


def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    
    gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    
fractal_rectangle((10, 10), (50, 10), (50, 50), (10, 50))