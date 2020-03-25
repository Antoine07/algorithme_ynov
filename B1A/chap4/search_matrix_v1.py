

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


def search_matrix_word(w, m):

    s = []

    for l in m:
        s.append( search_word(w, l) )

    return s

print(search_matrix_word(w, A))
