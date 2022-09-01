def permuting(a,b,k):
    a.sort()
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i]+b[i]<k:
            return "NO"
    else:
        return "YES"
print(permuting([1,2,3],[7,8,9],10))


