

def search_word(w, l):

    j = 0

    for i in range(len(l)):
        
        if w[j] == l[i]:
            print("rouver en ", i)
            j = j + 1
        else:
            j = 0

        # On a rouvé w dans l
        # Décallage car on commence à compter à partir de 0
        if j == len(w):
            return i - ( len(w) - 1 )  

    return None

w = [1,2,3]
l = [7,2,1,2,3,5]

# On sait qu'à partir de k le mot commence dans l
# k est l'indice de début du mot recherché dans la liste
k = search_word(w, l)

if k != None:
    for i in range(len(w)):
        l[ k + i ] = None

print(l) 

def search_replace_list(w, l):
    k = search_word(w, l)

    if k != None:
        for i in range(len(w)):
            l[ k + i ] = None

    return l

A = [
    [5, 3, 1, 2, 3, 7],
    [7, 8, 4, 3, 8, 11],
    [8, 1, 2, 3, 7, 9],
    [3, 2, 1, 2, 3,1],
    [1, 2, 3 , 1 ,2, 3 ],
]

w = [1, 2, 3]

for l in A:
    search_replace_list(w, l)

print(A)


def search_replace_matrix(w, m):

    for l in m:
        search_replace_list(w, l)

    return m