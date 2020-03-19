
def create_matrix(n, v):
    m = []
    # _ permet de ne pas prendre de variable pour récupérer un indice
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(v)
        m.append(row)

    return m

print( create_matrix(5, 0) )
