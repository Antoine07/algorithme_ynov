

def sum_func(f, n):
    s = 0
    for i in range(1, n + 1):
        s += f(i)

    return s

def square(x):
    return x**2

print( sum_func(square, 10) )

# Somme des 10 premiers cubes
print( sum_func( lambda x : x**3, 10 ))