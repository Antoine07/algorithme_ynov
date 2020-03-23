

def myFunc():
    a = 4

# la valeur d'une fonction qui ne retourne rien est None
print(myFunc())


# On appelle pas la fonction et pourtant Python voit ça comme une valeur
print(myFunc)


def square(x):
    return x**2

# Retourne une fonction lambda donc une fonction
def compose(f):

    return lambda x : f(x)

print( compose(square)(9) )

