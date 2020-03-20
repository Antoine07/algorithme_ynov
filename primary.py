

import math

n = int(input("Donnez un nombre n entier \n"))

isPrimary = True
count = 0
# En maths on montre que si on a pas trouvé de diviseur d à n inférieur à math.sqrt(n) alors on peut affirmer que n est premier
max_d = math.sqrt(n) 
d = 2
while d < max_d:

    count+=1

    if n % d == 0:
        isPrimary = False
        break

    d += 1
    
print(n, isPrimary, count)