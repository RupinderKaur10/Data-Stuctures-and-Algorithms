import math

def egyptianFraction(nr,dr):
    print("The Representation of {0}/{1} is".format(nr,dr),end="\n")

    denom = []
    while nr != 0:
        n = math.ceil(dr/nr)
        denom.append(n)
        nr = n*nr-dr
        dr = n*dr

    for i in range(len(denom)):
        if i != len(denom)-1:
            print("1/{0} +".format(denom[i]),end=" ")
        else:
            print("1/{0}".format(denom[i]),end=" ")

egyptianFraction(12,13)
