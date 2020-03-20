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
    
    l = len(m)
    c = len(m[0])

    return l, c

def sum_matrix(m, p):

    """
        l, c = dimension(m) 
        a, b = dimension(p)
    """
    # On vérifie qu'elles ont les mêmes dimensions
    if dimension(m) == dimension(p):
        l, c = dimension(m)
        s = create_matrix(l, c, 0)

        for i in range(l):
            for j in range(c):
                s[i][j] = m[i][j] + p[i][j]

        return s
        
    else:
        # Valeur qui ne pose pas de problème dans un programme "neutre"
        return None

A = [
    [3,7,5],
    [2,8,8],
    [7,9,9]
]

B = [
    [1,2,1],
    [1,1,0],
    [2, 1, 3]
]

print(sum_matrix(A, B))