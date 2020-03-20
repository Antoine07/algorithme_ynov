
def create_matrix(n, v):
    m = []
    
    for _ in range(n):
        row = []
        # pour créer une ligne
        for _ in range(n):
            row.append(v)
        # ajouter une ligne à m la matrice finale
        m.append(row)
    
    return m

print(create_matrix(5, 0))