#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:47:09 2019

@author: aleksandr
"""

def choise_sort():
    A = [5, 4, 3, 2, 1]
    A_sorted = [1, 2, 3, 4, 5]
    
    n = len(A)
    
    for pos in range(0, n-1):
        for next_pos in range(pos+1, n):
            if A[next_pos] < A[pos]:
                print(A)
                A[pos], A[next_pos] = A[next_pos], A[pos]
                print(A)
    print("ok"  if A == A_sorted else "fail")
        
choise_sort()