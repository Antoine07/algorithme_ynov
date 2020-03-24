

# rechercher un indice dans une liste
def search_indice_v1(x, l):

    for i in range(len(l)):
        if x == l[i]:
            return i

    return None

print(search_indice_v1(71, [1,2,3,5,7]))

def search_indice_v2(x, l):
    i = 0

    while i < len(l) and x != l[i]:
        i += 1

    if i < len(l):
        return i

    return None

print(search_indice_v2(7, [1,2,3,5,7]))

# Comme une chaîne de caractères se parcourt comme une liste 
# on peut utiliser les fonctions de recherche déjà développées
print( search_indice_v1("j", "bonjour le monde") )

print( search_indice_v2("j", "bonjour le monde"))
