

def appartient_v1(x, l):

    for e in l:
        if x == e:
            return True

    return False

print(appartient_v1(20, [1,2,3]))

def appartient_v2(x, l):
    i = 0

    while i < len(l) and l[i] != x:
        i += 1
    
    return i < len(l)

print(appartient_v2(3, [1,2,3]))
