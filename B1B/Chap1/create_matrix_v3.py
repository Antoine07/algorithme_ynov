
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

print(create_matrix(5,3, 0))

def dimension(m):
    l, c = 4, 3

    return l, c

a, b = dimension([[1,2]])

print(a, b)