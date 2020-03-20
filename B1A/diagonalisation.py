

def create_matrix(l, c, v):

    # création d'une liste
    m = []
    for _ in range(l):
        row = []
        for _ in range(c):
            row.append(v)
        m.append(row)

    return m

def create_diagonalisation_v1(n, v):
    m = create_matrix(n, n, 0)

    for i in range(n):
        for j in range(n):
            if i == j :
                m[i][j] = v
    
    return m

print(create_diagonalisation_v1(4, 7))

# Réduction du nombre d'instructions en trouvant une astuce
def create_diagonalisation_v2(n, v):
    m = create_matrix(n, n, 0)

    for i in range(n):
        m[i][i] = v

    return m

print(create_diagonalisation_v2(4, 7))