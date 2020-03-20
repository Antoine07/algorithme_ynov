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

def transpose(a):
    # on récupère les dimensions de la matrice
    # l = 2, c = 3
    l, c = dimension(a)

    # Matrice qui aura les dimensions de la matrice transposée
    # matrice rempli pour l'instant que de 0, matrice temporaire
    t = create_matrix(c, l, 0)
    """
    t =
        [
            [0, 0],
            [0, 0],
            [0, 0]
        ]
    """

    for i in range(l):
        for j in range(c):
            print(a[i][j])

    for i in range(c):
        for j in range(l):
            # i = 0 et j 0, 1
            # 0, 0    0 , 0  --> 3
            # 0, 1    1 , 0  --> 7

            # i = 1 et j O, 1
            # 1, 0   0, 1  --> 2
            # 1, 1   1, 1  --> 8

            # i = 2 et j 0, 1
            # 2, 0   0, 2  -->  7
            # 2, 1   1, 2  -->  9
            t[i][j] = a[j][i]

    return t

A = [
    [3 ,2 ,7 ], # 3 : (0, 0) 2 : (0, 1) 7 : (0 , 2)
    [7, 8, 9 ]  # 7 : (1, 0) 8 : (1, 1) 9 : (1 , 2)
]

print(transpose(A))

"""
[
    [3, 7],  # 3 : (0, 0)  7 : (0, 1)
    [2, 8],  # 2 : (1, 0)  8 :  (1, 1)
    [7, 9]   # 7 : (2, 0)  9 :  (2, 1)
]

"""

B = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

"""
Btranspose = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]
]
"""

print(transpose(B))
