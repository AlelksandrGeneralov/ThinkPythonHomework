#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:26:02 2019

@author: aleksandr
"""

#import time


def add_in_list():
    """create a list from txt file"""   
    t = open('words.txt')
    t1 = []
    for line in t:
        word = line.strip()
        t1.append(word)
    return t1

def linare_search(data, target):
    """linar search in list"""
    for i in range(0, len(data)-1):
        if target == data[i]:
            return True
            print(True)
    return False
    print(False)

def binary_search_interactive(data, target):
    """interactive binary search"""
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
            print(True)
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False
    print(False)
    
def binary_search_recursive(data, target, low, high):
    """recusieve binary search"""
    if low > high:
        return False
        print(False)
    else:
        mid = (low + high)//2
        if target == mid:
            return True
            print(True)
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        return binary_search_recursive(data, target, mid+1, high)
    return False
    print(False)          

def timer():
    import time
    
    start_time = time.time()
    print('test for: ', linare_search.__doc__)
    print(linare_search(add_in_list(), 'aaah'))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'sec')

    start_time = time.time()
    print('test for: ', binary_search_interactive.__doc__)
    print(binary_search_interactive(add_in_list(), 'aaah'))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'sec')

    start_time = time.time()
    print('test for: ', binary_search_recursive.__doc__)
    print(binary_search_recursive(add_in_list(), 'aaah', 0, len(add_in_list())-1))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'sec')

if __name__ == "__main__":
    timer()
