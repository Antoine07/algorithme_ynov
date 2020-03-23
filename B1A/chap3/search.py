
def appartient_v1(x, l):

    for y in l:

        if y == x:
            return True 
    
    return False

def appartient_v2(x, l):
    i = 0

    while i < len(l) and l[i] != x :
        i +=1

    # si c'est plus petit que la longueur de la liste alors je l'ai trouvé et
    # la fonction renvoie True et sinon i == len(l) dans ce cas je ne l'ai pas trouvé
    return i < len(l)