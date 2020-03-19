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

    number_inverse = 0
    power = len(digit) - 1
    for i in range(0, len(digit)):
        #print(digit[i] * 10**( power - i ))
        number_inverse = number_inverse + digit[i] * 10**( power - i )

    print(number_inverse)

"""
72341

7 0000 = 7 * 10**4
+
2000
+
300
+
40
+
1

"""