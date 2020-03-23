
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
def maxGen(*numbers):

    # print(numbers)

    for u in numbers:
        print(u)

print(maxGen(1,2,3,4,5,6))