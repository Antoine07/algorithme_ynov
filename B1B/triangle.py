"""
Une boucle qui dépend d'une autre boucle
"""

# hauteur du triangle
n = 5

# n = 5 i in [0, 1, 2, 3, 4]
for i in range(n):
    # i=0 :0 , i=1 : 0,1, i=2 : 0,1,2, i=3 :0,1,2,3, i =4 0,1,2,3,4, ...
    for j in range(i + 1):
        print('*', end="")
    print()
