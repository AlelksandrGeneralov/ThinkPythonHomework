#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:05:32 2019

@author: aleksandr
"""

def bubble_sort():
    A = [5, 4, 3, 2, 1]
    A_sorted = [1, 2, 3, 4, 5]
    
    n = len(A)
    
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if A[k] > A[k+1]:
                print(A)
                A[k], A[k+1] = A[k+1], A[k]
                print(A)
    print("ok" if A == A_sorted else "fail")
    
bubble_sort()