
n = 5

for i in range(n):
    # une deuxième boucle peut dépendre d'une première boucle
    for j in range(i+1):
        print("*", end="") # end = "\n" et end="" ne fera pas de retour à la ligne
    print()
