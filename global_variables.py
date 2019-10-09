
verbose = True
been_called = False
count = 0
known = {0: 0, 1: 1}


def example():
    if verbose:
        print('running example')


def example2():
    been_called = True
    if been_called:
        print('running example 2')


def example3():
    global been_called
    been_called = True
    if been_called:
        print('running example 3')


def counter():
    global count
    count += 1
    print(count)


def example4():
    known[2] = 2
    print(known)


def example5():
    global known
    known = dict()
    known[count] = count
    print(known)


example()
example2()
example3()
counter()
example4()
example5()
