

def myMap(l, func):

    for i in range(len(l)):
        # on peut appliquer un calcul sur chaque élément de notre liste
        # avec une fonction qui n'est pas encore définie
        l[i] = func( l[i] )

    return l

def square(x):

    return x**2

print([1,2,3,4])

print( myMap( [1,2,3,4] , square) )

def augmentation(x):

    return x + x*0.5

print( myMap( [1,2,3,4] , augmentation) )
