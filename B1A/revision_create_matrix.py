
# l : lignes et c : colonnes
def create_matrix_show(l, c, v):

    for _ in range(l):
        for _ in range(c):
            print(v, end="")
        print()

# create_matrix_show(5, 3, 0)

def create_matrix(l, c, v):

    # création d'une liste
    m = []
    for _ in range(l):
        row = []
        for _ in range(c):
            row.append(v)
        m.append(row)

    return m

A = create_matrix(5, 3, 0)
# print(A)


"""
A = [
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3],
]

4 X 3

"""

B = [
    [1,2,3], # 0
    [1,2,3], # 1  <--
    [1,2,3], # 2
    [1,2,3], # 3
    [1,2, 3], # 4
]

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

# print( type( dimension(B) ) )

# a et b
# a, b, c = 12, 8, 11
# assigner les valeur retourner par la fonction dimension pour a, b
a, b = dimension(B)

A = [
    [2, 1, 3],
    [4 ,5, 7]
]

l, c = dimension(A)
Atrans = create_matrix(c, l, 0)
# print(Atrans)

for i in range(c):
    for j in range(l):
        # print(Atrans[i][j], end ="")
        Atrans[i][j] = A[j][i]

print(Atrans)