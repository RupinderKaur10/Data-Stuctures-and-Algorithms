a = [-1,2,1,-4]
def printCombination(a,n,r):
    data = [0]*r
    combinationUtil(a,n,r,0,data,0)
def combinationUtil(a,n,r,index,data,i):
    if index == r:
        for j in range(r):
            print(data[j],end = " ")
        print()
        return
    if i>=n:
        return
    data[index] = a[i]
    combinationUtil(a,n,r,index+1,data,i+1)
    combinationUtil(a,n,r,index,data,i+1)
n = len(a)
r=3
printCombination(a,n,r)
