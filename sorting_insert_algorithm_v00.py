#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:16:19 2019

@author: aleksandr
"""

def insert_sort():
    A = [5, 4, 3, 2, 1, 2]
    A_sorted = [1, 2, 3, 4, 5, 2]
#    print(A)
    
    n = len(A)
    
    for top in range(1, n):
        k = top
#        print(A)
        while k > 0 and A[k-1] > A[k]:
#            print(A)
            A[k], A[k-1] = A[k-1], A[k]
            print(A)
            k = k-1
    print("ok" if A == A_sorted else "fail")

insert_sort()         
        
        