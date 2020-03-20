
n = int(input("Donnez un nombre entier \n"))

divisors = []
d = 1

while d <= n:

    if n % d == 0:
        divisors.append(d)
    
    d += 1

print(divisors)

# deuxième version

divisors = []

for d in range(1, n + 1):
    if n % d == 0:
        divisors.append(d)

print(divisors)
