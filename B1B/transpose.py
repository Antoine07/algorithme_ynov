def create_matrix(l, c, v):
    m = []
    
    for _ in range(l):
        row = []
        # pour créer une ligne
        for _ in range(c):
            row.append(v)
        # ajouter une ligne à m la matrice finale
        m.append(row)
    
    return m

def dimension(m):
    # l = len(m) # nombre de lignes
    # c = len(m[0]) # dimension sur les colonnes
    l, c = len(m), len(m[0])

    return l, c

def transpose(m):
    # on récupère les dimensions de la matrice
    # l = 2, c = 3
    l, c = dimension(m)

    # Matrice qui aura les dimensions de la matrice transposée
    t = create_matrix(c, l, 0)

    for i in range(c):
        for j in range(l):
            #print(m[i][j])
            t[i][j] = m[j][i]


    return t

A = [
    [3,2,7],   # 0,0 : 3  0,1 : 2, 0,2 : 7
    [7,8,9]
]

print(transpose(A))