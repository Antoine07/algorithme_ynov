
n = 12347
#print( 1237 % 10 )
#print( 12370 % 10 )

if n % 10 == 0:
    print("On ne peut pas inverser ce nombre unité 0...")
elif n < 10:
    print("Pas d'inversion possible :", n)
else:
    n = str(n)
    head = n[0]
    #queue = n[len(n) - 1]
    queue = n[-1] # Python pour avoir le dernier élément d'une chaîne
    #print(queue)
    middle = ''
    # range commence à O et s'arrêtera à longueur - 1
    for i in range(1, len(n) - 1):
        middle = middle + n[i]

    number_inverse = queue + middle + head
    print(type(number_inverse)) # chaîne de caractères

    number_inverse = int(number_inverse)
    print(number_inverse)
    print(type(number_inverse)) # int


# En considérant n comme un entier
n = 12347
digit = []

if n % 10 == 0:
    print("On ne peut pas inverser ce nombre unité 0...")
elif n < 10:
    print("Pas d'inversion possible :", n)
else:
    while n > 0:
        # print(n % 10)
        digit.append(n % 10)
        n = n // 10 # division entière pas de virgule
        # print(n)
    digit.reverse() # Permet d'inverser les éléments d'une liste
    #print(digit)

    tmp = digit[0]
    digit[0] = digit[-1]
    digit[-1] = tmp

    print(digit)

    number_inverse = ''
    for i in range(0, len(digit)):
        number_inverse = number_inverse + str( digit[i] )

    number_inverse = int(number_inverse)
    print(number_inverse)
