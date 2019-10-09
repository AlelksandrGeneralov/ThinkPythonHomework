t = 'a',
print(type(t))

t2 = ('a')
print(type(t2))

t3 = tuple()
print(type(t3))

t4 = tuple('lupins')
print(t4)
print(t4[0])
print(t4[1:4])

# t4[0] = 'a'

t5 = t4 + ('A',)
print(t5)

adr = 'monty@python.org'
uname, domain = adr.split('@')
print(uname, domain)

print(divmod(5, 2))


def min_max(a):
    return min(a), max(a)


print(min_max(t4))


def printall(*args):
    return args


print(printall(t4))


def sumall(*args):
    a = (1, 2, 3, 4, 5)
    return(sum(a))


print(sumall())

a = 'abc'
b = [1, 2, 3]
c = zip(a, b)
for letter, number in c:
    print(letter, number)


def has_match(a, b):
    a = [1, 2, 3, 4]
    b = [1, 1, 3]
    for x, y in zip(a, b):
        if x == y:
            return True
    return False


print(has_match(a, b))

for index, element in enumerate('abc'):
    print(index, element)


d = {'a': 1, 'b': 2, 'c': 3}
t = d.items()
print(t)

d1 = dict(zip('abc', range(3)))
print(d1)

for key, value in d.items():
    print(key, value)


# comparing tuples
