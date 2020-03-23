"""

Un nombre premier c'est un nombre qui n'a que deux diviseurs 1 et lui-même

Théorème que l'on peut trouver en Maths
Si il n'y a pas de diviseur d inférieur à racine de n alors n est premier

"""

import math

n = int(input("Donnez un nombre entier \n"))

count = 1
d = 2

# flag boolean
isPrimary = True

while True:

    if n % d == 0:
        isPrimary = False
        break

    d += 1

    # Si d est supérieur ou égal à racine carré du nombre n
    # On arrête la recherche des diviseurs d
    if d >= math.sqrt(n):
        isPrimary = True
        break

    count += 1


if isPrimary:
    print("Ce nombre {} est premier".format(n))
else:
    print("Ce nombre {} n'est pas premier".format(n))

print("nombre de boucle(s) {}".format(count))