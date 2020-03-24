import random

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

def create_matrix(l, c, v):

    # création d'une liste
    m = []
    for _ in range(l):
        row = []
        for _ in range(c):
            row.append(v)
        m.append(row)

    return m

def search_word(w, l):

    for i in range( len(l) - len(w) + 1 ):
        j = 0

        while j < len(w) and w[j] == l[i + j]:
            j += 1

        if j == len(w):
            return i

    return None


matrix = create_matrix(5, 5, 0)

for i in range(5):
    for j in range(5):
        matrix[i][j] = random.randint(1, 3)

w = [1, 2]
print(w)
print(matrix)

def search_matrix(w, matrix):
    l, c = dimension(matrix)
    m = create_matrix(l, c, False)

    for i in range(l):
        j = search_word(w, matrix[i])
        if j != None:
            m[i][j] = True

    return m

print( search_matrix(w, matrix) )