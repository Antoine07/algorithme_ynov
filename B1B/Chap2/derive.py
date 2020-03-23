

def derive(f, esp):

    return lambda x : ( f( x + esp ) - f(x) ) / esp

def square(x):

    return x**2

# ici on calcule la dérivée de x**2 en 3
print( derive(square, 0.000001)(3) )

# 2x3
print(2*3)