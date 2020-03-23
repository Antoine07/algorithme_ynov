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


# Exemple de fonction qui retourne une fonction

def compose_v1(f):

    def myLambda(x):

        return f(x)

    return myLambda

# Il retourne une fonction
print( compose_v1(square) )

# On retourne la fonction et l'on appelle en lui passant une valeur
print( compose_v1(square)(8) )

# On met la fonction retournée dans une variable
s = compose_v1(square)

# Appeler la fonction que l'on a mis dans une variable
s(10)

# Meme chose avec une fonction lambda
def compose_v2(f):

    return lambda x: f(x)



# la fonctio otherFunc est une fonction qui a un paramètre
# otherFunc(x)
def myFunc(x, otherFunc):

    return otherFunc(x)

print( 'ici', myFunc(10, square) )


def myFunc2(otherFunc):

    return lambda x: otherFunc(x)

print(myFunc2(square)(8))

print(square )