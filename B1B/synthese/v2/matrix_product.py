

def dimension(m):
    l, c =  len(m), len(m[0])

    return l, c

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

def mult_matrix(a, b):
    # n ligne p colonne
    n, p = dimension(a)
    # q ligne r colonne
    q, r = dimension(b)

    # Le nombre de colonnes p de la première matrice
    # Doit être égale au nombre q de lignes de la deuxième matrice
    assert q == p

    c = create_matrix(n, r, 0)

    for i in range(n):
        for j in range(r):
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]

    return c
