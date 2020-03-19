
def create_matrix(l,c,v):
    m = []
    # _ permet de ne pas prendre de variable pour récupérer un indice
    for _ in range(l):
        row = []
        for _ in range(c):
            row.append(v)
        m.append(row)

    return m

print( create_matrix(5, 7, 0) )
