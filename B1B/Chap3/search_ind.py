
# Recherche de l'indice avec une boucle for
def search_indice_v1(x, l):

    for i in range(len(l)):

        if l[i] == x :
            return i

    return None

print( search_indice_v1(7, [1,2,7,9,3,100]) )

# Une deuxième version de la recherche de la position d'un indice
def search_indice_v2(x, l):
    i = 0
    while i <len(l) and l[i] != x:
        i += 1

    if i < len(l):
        return i

    return None

