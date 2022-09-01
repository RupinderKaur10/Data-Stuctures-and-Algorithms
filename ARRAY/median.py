from statistics import median
a = [5,15,1,3]
l = 0
r =1
b = []
res = []
while r<=len(a):
    for i in range(l,r):
        b.append(a[i])
    res.append(int(median(b)))
    r+=1
    l+=1
print(res)

