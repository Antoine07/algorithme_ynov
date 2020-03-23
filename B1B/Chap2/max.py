def max3(u,v,w):

    def max2(a, b):

        if a > b:
            return a

        return b

    return max2(u, max2(v,w) )

print(max3(100,20,3))

def max4(u,v,w, p):

    def max2(a, b):

        if a > b:
            return a

        return b

    return max2(u, max2(v, max2(w,p)))

print(max4(1000,200,30, 4))

# Comme exercice essayez généraliser avec une fonction maxGen

#unpacking 
def maxGen( *numbers ):

    print(numbers)

    for number in numbers:
        print(number)

maxGen(1,2,3,4,5,6,7,8,9)
maxGen(1,2,3)
