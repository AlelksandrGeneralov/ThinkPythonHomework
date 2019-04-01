#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def square_numbers_1(data):
	'''fill in list with "append" '''
 	t = []
 	for i in data:
 		t.append(i*i)
 	return(t)


def square_numbers_2(data):
	'''fill in list with "yield" gentrator'''
 	for i in data:
 		yield (i*i)


def square_numbers_3(data):
	'''fill in list with complex argument'''
	my_data = [x*x for x in data]
	return(my_data)


def square_numbers_4(data):
	'''fill in list with "print list(arg)" '''
	my_data = (x*x for x in data)
	return(list(my_data))

def timer():

    import time
    
    data = [1, 2, 3, 4, 4]

    start_time = time.time()
    print 'test for: ', square_numbers_1.__doc__
    print(square_numbers_1(data))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'sec')

    start_time = time.time()
    print 'test for: ', square_numbers_2.__doc__
    my_data = square_numbers_2(data)
    for num in my_data:
    	print(num)
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'sec')

    start_time = time.time()
    print 'test for: ', square_numbers_3.__doc__
    print(square_numbers_3(data))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'sec')

    start_time = time.time()
    print 'test for: ', square_numbers_4.__doc__
    print(square_numbers_4(data))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'sec')

if __name__ == "__main__":
    timer()
