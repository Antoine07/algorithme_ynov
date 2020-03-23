

def search(l, n):

    for i in range( len(l) ):

        if l[i] == n:
            return True
    
    return (i + 1)

print(search([8,9,1], 11))