

def search(n, l):

    for i in range(len(l)):
        # print(l[i])
        if n == l[i]:
            return True

    return False


print( search(7, [8,9,7,10]) )