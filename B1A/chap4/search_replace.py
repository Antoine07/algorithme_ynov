

def search_word(w, l):

    j = 0
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
            return i - ( len(w) - 1 )
        
    # On pas trouvé le mot
    return None

A = [
    [5, 3, 1, 2],
    [7, 8, 4, 3],
    [8, 1, 2, 4],
    [3, 2, 1, 2],
    [1, 2, 1, 2]
]

w = [1, 2]

def search_replace_matrix(w, m):

    # i donne l'indice de la ligne de la matrice
    for i in range( len(m) ):
        # j soit une valeur entière soit None
        k = search_word(w, m[i])

        if k != None:
            for j in range(len(w)):
                m[i][k + j] = None

    
    return m

print(search_replace_matrix(w, A))