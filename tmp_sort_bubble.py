#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:09:52 2019

@author: aleksandr
"""

def sort():
    A = [5, 4, 3, 2, 1]
    
    n = len(A)
#    print("n = ", n)
    
    for b in range(1, n):
#        print("b = ", range(1, n))
        for k in range(0, n-b):
            if A[k] > A[k+1]:
#                print("A[k] = ", A[k])
#                print("A[k+1] = ", A[k+1])
                A[k], A[k+1] = A[k+1], A[k]
#                print("k = ", range(0, n-b))
                print(A)
#    print(A)
    
sort()
    