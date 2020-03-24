

def search_word_v1(w, l):

    for i in range( len(l) - len(w) + 1 ):
        j = 0

        while j < len(w) and w[j] == l[i + j]:
            j += 1

        if j == len(w):
            return i

    return None
        
print( search_word_v1([1,2], [1, 3, 5, 1,2 ]) )