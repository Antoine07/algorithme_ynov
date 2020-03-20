

def search_v1(n, l):

    for i in range(len(l)):
        # print(l[i])
        if n == l[i]:
            return True

    return False


print( search_v1(7, [8,9,7,10]) )


def search_v2(n, l):

    for num in l:
        # print(num)
        if num == n:
            return True

    return False

print( search_v2(71, [8,9,7,10]) )

# attention lorsque vous parcourez une liste il faut savoir ce que vous parcourez.
B = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

for b in B:
    print(b)