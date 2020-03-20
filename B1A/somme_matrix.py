def create_matrix(l, c, v):

    # création d'une liste
    m = []
    for _ in range(l):
        row = []
        for _ in range(c):
            row.append(v)
        m.append(row)

    return m

def dimension(m):
    l = len(m)
    c = len(m[0])

    # on vérifie la cohérence des dimensions
    # c'est dire ici que toutes les lignes on bien la même dimension
    for i in range(1, l):
    # assert arrête le programme 
       assert c == len(m[i]) 

    # En Python on peut retourner deux valeurs dans le script, on renvoit un tuple Python
    # un tuple c'est une structure de données comme une liste par exemple
    return (l, c)

def sum_matrix(m, p):

    # a, b == c, d
    if dimension(m) == dimension(p) :
        l, c = dimension(m)
        s = create_matrix(l, c, 0)

        for i in range(l):
            for j in range(c):
                s[i][j] = m[i][j] + p[i][j]

        return s
    else:
        return None

A = [
    [3, 7, 5],
    [2, 8, 8],
    [7, 9, 9]
]

B= [
    [1, 2, 1],
    [1,1,0],
    [2,1,3]
]

print(sum_matrix(A, B))