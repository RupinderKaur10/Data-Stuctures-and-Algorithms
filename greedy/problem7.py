n = 5
k = 2
count=0
for i in range(1,n+1):
    kk = k-1
    if kk !=0:
        for j in range(i,n+1):
            if j%i == 0:
                print(j,i)
                count+=1
    else:
        count+=1
print(count)