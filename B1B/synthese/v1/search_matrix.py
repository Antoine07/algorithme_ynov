def search_word(w, l):
    j = 0
    for i in range(len(l)):

        if w[j] == l[i]:
            j += 1
        else:
            j = 0

        if j == len(w):
            # comme on compte à partir de zéro
            # On retire la longueur de la liste - 1
            # tout est décalé
            return i - ( len(w) - 1 )

    return None

A = [
    [5, 3, 1, 2],
    [7, 8, 4, 3],
    [8, 1, 2, 4],
    [3, 2, 1, 2],
    [1, 2, 1, 2],
]

w = [1, 2]

s = []

for l in A:
    # print(l)
    # print(search_word(w,l))
    s.append( search_word(w,l) )

print(s)

def search_matrix_word(w, m):
    s = []

    for l in m:
        s.append( search_word(w,l) )

    return m