
# On a une formule générale pour estimer la valeur d'une dérivée en un point donné
def derive(f,esp):

    return lambda x : ( f(x + esp) - f(x) ) / esp 


# fonction carré
def square(x):

    return x*x

# Calculer la dérivée de la fonction  x**2 en 1
print( derive(square, 0.000001)(1) )

# On sait que la dérviée de x**2 c'est 2x en 1
print( 2*1 )