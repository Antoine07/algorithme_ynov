

# Exercice 1
def mult(l, m):

    if len(l) != len(m):
        return None

    res =  []
    for i in range(len(l)):
        res.append(l[i] * m[i])

    return res

print(mult([1,2,3,4], [1,2,3,4]))

# Exercice 2
def number_max(l):

    m = l[0]

    for i in range(1, len(l)):

        if l[i] > m:
            m = l[i]

    return m

print(number_max([1,2,30,4]))

# Exercice 3
N = 10
solutions = []
for a in range(N):
    for b in range(N):
        if a + b == 10 and a <= b :
            # On range les couples de valeurs dans un tuple (a, b)
            solutions.append((a, b))

print(solutions)