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

def create_diagonale_v1(n, v):
    m = create_matrix(n, n, 0)

    for i in range(n):
        for j in range(n):
            if i == j:
                m[i][j] = v
    
    return m

print(create_diagonale_v1(7, 3))

def create_diagonale_v2(n, v):
    m = create_matrix(n, n, 0)

    for i in range(n):
        m[i][i] = v

    return m

print(create_diagonale_v2(7, 3))
