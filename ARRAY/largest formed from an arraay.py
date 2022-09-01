def LargestNumber(a,n):
    res =""
    if n == 1:
        return a[0]
    for i in range(n):
        a[i] = str(a[i])
    for i in range(n):
        for j in range(i+1,n):
            if a[j]+a[i]>a[i]+a[j]:
                a[i],a[j] = a[j],a[i]
    for i in a:
        res+=i
    return res
print(LargestNumber([54,546,548,60],4))