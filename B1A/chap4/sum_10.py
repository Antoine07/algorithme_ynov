
N = 10

solutions = []

for i in range(N):
    for j in range(N):
        # pour exclure les symétriques on peut mettre i <= j
        if i + j == 10 and i <= j :
            solutions.append((i, j))

print(solutions)