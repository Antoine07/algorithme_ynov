

def max3(u,v,w):

    def max2(a, b):
        # un return vous fait sortir de la fonction
        if a > b:
            return a

        return b

    return max2(u, max2(v, w) )

print(max3(800,100,80))