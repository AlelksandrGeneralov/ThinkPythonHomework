
verbose = True
been_called = False


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


example()
example2()
example3()
