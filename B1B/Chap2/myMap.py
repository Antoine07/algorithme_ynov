

def myMap(l, func):

    for i in range(len(l)):
        l[i] = func(l[i])

    return l

def square(x):

    return x**2