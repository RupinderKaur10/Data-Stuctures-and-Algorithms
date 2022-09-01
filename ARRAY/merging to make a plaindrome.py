a = [11,14,15,99]
i,j = 0,len(a)-1
count = 0
while i<=j:
    if a[i] == a[j]:
        i+=1
        j-=1
    if a[i]!=a[j]:
        mer = a[i]+a[j]
        a[i] = mer
        a[j] = mer
        i+=1
        j-=1
        count+=1
print(a,"\n",count)
