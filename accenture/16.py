def SumOfTable(n):
    a=[]
    sum = 0
    for i in range(0,10*n+1,n):
        a.append(i)
        sum+=i
    for i in range(1,len(a)):
        print(a[i],end=" ")
    return f"\n{sum}"
print(SumOfTable(5))