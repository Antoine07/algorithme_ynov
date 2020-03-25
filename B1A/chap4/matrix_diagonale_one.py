
def create_matrix(l, c, v):

    # création d'une liste
    m = []
    for _ in range(l):
        row = []
        for _ in range(c):
            row.append(v)
        m.append(row)

    return m



# On peut passer un v = 1 dans les paramètres pour initialiser une valeur
def create_diagonalisation_sup_inf(n, v = 1):
    m = create_matrix(n, n, 0)

    for i in range(n):
        for j in range(n):
            if i == j :
                m[i][j] = v
                if j < (n - 1):
                    m[i][j+1] = 1
                if j > 0:
                    m[i][j-1] = 1
    
    return m

print(create_diagonalisation_sup_inf(5, v = 1))