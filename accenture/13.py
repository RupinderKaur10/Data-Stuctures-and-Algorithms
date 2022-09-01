def MaxExponents(a,b):
    maxx = []
    count = 0
    res = {}
    for i in range(a,b):
        while i%2==0 and i!=0:
            count+=1
            i = i//2
        res[i] = count
        count=0
    return max(res.values())
print(MaxExponents(7,12))

