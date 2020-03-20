
n = int(input("Donnez un nombre entier"))

divisors = []
d = 1

while d < n :
    if n % d == 0 :
        divisors.append(d)
    d += 1

print(divisors)