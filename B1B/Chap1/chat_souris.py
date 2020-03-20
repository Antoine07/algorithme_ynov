def eat_mouse(n, nbMouses = 13):
    mouses = [ i for i in range(1, nbMouses + 1)]
    solution = []
    step = (n - 1)  % len(mouses)
    solution.append(mouses[step])

    # Le chat mange la souris
    del mouses[step]

    # tant qu'il y a des souris le chat mange ...
    while  len( mouses) > 0 :
        # la liste diminue ...Donc le modulo aussi
        step = (step + n - 1) % len(mouses)
        solution.append(mouses[step])
        del mouses[step]

    return solution

print(eat_mouse(5))

n = 1

while eat_mouse(n)[-1] != 1:
    n += 1

print(f"voici le bon saut pour terminer sur la souris blanche : {n}")
print(eat_mouse(n))
