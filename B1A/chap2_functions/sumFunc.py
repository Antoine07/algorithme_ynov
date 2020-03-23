
def sum_func(f, n):
    s = 0

    for i in range(n+1):
        s = s + f(i)

    return s

def square(x):

    return x*x

print(sum_func(square, 10))