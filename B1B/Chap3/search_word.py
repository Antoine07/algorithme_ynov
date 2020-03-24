

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


print(search_word([1,2], [6, 7, 8, 1, 2, 9]))

print(search_word("bonjour", "Hello il y a bonjour dans la chaîne"))