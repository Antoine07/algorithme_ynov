def myFuncNone():
    print("Hello my function")

# La valeur de la fonction c'est None ici car elle ne retourne rien
print( myFuncNone() )


# myMap


# Pour Python l est une liste et f une fonction ou un plus précisément un callable
def myMap(l, f):

    for i in range(len(l)):
        l[i] = f(l[i])

    return l

# square est bien compatible avec le paramètre f qui admet un paramètre 
def square(x):

    return x*x

print(myMap([1,2,3,4], square))
