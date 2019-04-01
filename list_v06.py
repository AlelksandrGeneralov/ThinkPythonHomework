#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:46:34 2019

@author: aleksandr
"""

import time

def add_in_list():    
    t = open('words.txt')
    t1 = []
    for line in t:
        word = line.strip()
        t1.append(word)
#    print(t1[15:])
    return(t1)

def is_in_list(lst, myword):
    
    avg_lst_rng = len(lst)//2
    print(lst[avg_lst_rng])
    print(avg_lst_rng)

    if len(lst) == 0 or len(lst) == 1 and lst[0] != myword:
        print(False)
    if myword == lst[avg_lst_rng]:
        print(True)
    if myword < lst[avg_lst_rng]:
        is_in_list(lst[:len(lst)//2], myword)
    if myword > lst[avg_lst_rng]:
        is_in_list(lst[len(lst)//2+1:], myword)

start_time = time.time()
is_in_list(add_in_list(), 'longshorema')
elapsed_time = time.time() - start_time
print(elapsed_time, 'sec')