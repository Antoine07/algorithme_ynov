
"""

Trouver un sous algo à un algo "complexe" pour aboutir à une solution 

"""

def max3(u,v, w):

    # Sous algorihtme que l'on sait faire rapidement
    def max2(a, b):
        if a > b:
            return a

        return b
    
    return max2( u, max2(v, w) )

print(max3(100,20,3))


def max4(u,v, w, p):

    # Sous algorihtme que l'on sait faire rapidement
    def max2(a, b):
        if a > b:
            return a

        return b
    
    return max2( max2( u, max2(v, w) ), p )

print(max4(1000,200,30, 4))


# Exercice à terminer faire un algorithme permettant de trouver le max d'un nombre quelconque de nombres
def maxGen_v1( *numbers ):
    # Python passe les paramètres dans un tuple
    # On n'est pas limité sur le nombre de valeurs dans la fonction

    def max2(a, b):

        if a > b:
            return a
        return b
    
    m = numbers[0]
    for i in range( 1, len( numbers) ):
        m = max2(m, numbers[i])
        
    return m

print(maxGen_v1(1,20,3,4,5,6))
print(maxGen_v1(100,2,3))
print(maxGen_v1(1000,2,3,4,500,6, 8, 9, 10))

def maxGen_v2(max2, *numbers):
    m = numbers[0]
    for i in range( 1, len( numbers) ):
        m = max2(m, numbers[i])
        
    return m

def max2(a, b):

    if a > b:
        return a
    return b

# Définir une fonction lambda dans une variable

"""
# Un ternaire en Python
# si a > b alors retourne a et sinon b
 a if a > b else b

"""

max2Lambda = lambda a, b: a if a > b else b
max2Lambda(1,2)

print(maxGen_v2(max2Lambda , 1,20,3,4,5,6))
print(maxGen_v2(max2Lambda , 100,2,3))
print(maxGen_v2(max2Lambda , 1000,2,3,4,500,6, 8, 9, 10))