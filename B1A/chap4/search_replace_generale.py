

def search_word(w, l):

    j = 0
    pos = []
    for i in range(len(l)):

        # à chaque fois qu'on a trouvé un élément dans la liste
        # qui correspond au incrémente j pour faire avancer
        # les indices du mot w
        if w[j] == l[i]:
            j += 1
        else:
            j = 0

        if j == len(w):
            # Position de l'i faire attention au décallage des indices
            pos.append( i - ( len(w) - 1 ) )
            # remettre à 0 pour la recherche pour être décallé
            j = 0
        
    # On pas trouvé le mot
    return pos

A = [
    [5, 3, 1, 2, 1, 2, 1],
    [7, 8, 4, 3, 9, 7, 8],
    [8, 1, 2, 4, 1, 0, 3],
    [3, 2, 1, 2, 1, 7, 8],
    [1, 2, 1, 2, 1, 2, 1]
]

w = [1, 2, 1]


def search_replace_matrix(w, m):

    # i donne l'indice de la ligne de la matrice
    for i in range( len(m) ):
        # j soit une valeur entière soit None
        pos = search_word(w, m[i])

        if len(pos) > 0:
            for k in pos:
                # On avance de la longueur du mot pour remplacer par None
                for j in range(len(w)):
                    m[i][k + j] = None

    
    return m

print(search_replace_matrix(w, A))
