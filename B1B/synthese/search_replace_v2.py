
# Changer cette fonction pour quelle retourne un tableau d'indice
def search_word(w, l):

    j = 0
    s = []
    for i in range(len(l)):
        
        if w[j] == l[i]:
            j = j + 1
        else:
            j = 0

        # On a rouvé w dans l
        # Décallage car on commence à compter à partir de 0
        if j == len(w):
            s.append(  i - ( len(w) - 1 )  )
            j = 0 # Pour reparcourir le mot

    return s

A = [
    [5, 3, 1, 2, 3, 7], # 1   [2]
    [7, 8, 4, 3, 8, 11], # 0 []
    [8, 1, 2, 3, 7, 9], # 1 [1]
    [3, 2, 1, 2, 3,1], # 1 [2]
    [1, 2, 3 , 1 ,2, 3 ], # 2 [0,3]
]

w = [1, 2, 3]


print(A)

for i in range(len(A)):
    
    # position des indices du mot recherché
    pos = search_word(w, A[i])

    # si il y a des indices du mot trouvé
    if len(pos) > 0:
        # je parcours mes indices de position
        for k in pos:
            # je parcours mon mot que je change en None dans la matrice
            for j in range(len(w)):
                A[i][k + j] = None


print(A)