def findSmallest(m,s):
    if s==0:
        if m==1:
            print("the smallest number is 0")
        else:
            print("Not Possible")
        return
    if s>9*m:
        print("not Possible")
        return
    res = [0]*(m+1)
    s-=1
    for i in range(m-1,0,-1):
        if s>9:
            res[i] = 9
            s-=9
        else:
            res[i] = s
            s=0

    res[0]= s+1
    for i in range(m):
        print(res[i],end="")
findSmallest(9,2)
