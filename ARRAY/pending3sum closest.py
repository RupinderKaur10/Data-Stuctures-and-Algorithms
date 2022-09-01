a = [-1,2,1,-4]
r = 3
n = len(a)
def combination(a,n,r):
    data = [0]*r
    combinationUtil(a,n,r,0,data,0)
def combinationUtil(a,n,r,index,data,i):
    x= 1
    summ = 0
    rs = []
    if index == r:
        for j in range(r):
            summ+=data[j]
        print(summ,"sum")
        rs.append(abs(summ-r))
        summ =0
        ini = min(rs)
        print(rs)
        for i in range(len(rs)):
            if rs[i]==ini:
                return rs[i]
        print()
        return
    if i>=n:
        return
    data[index] = a[i]
    combinationUtil(a,n,r,index+1,data,i+1)
    combinationUtil(a,n,r,index,data,i+1)
print(combination(a,n,r))
# x = 1
# i = 0
# summ = []
# r = []
# for i in range(len(a)):
#     for j in range(i+1,len(a)-1):
#         summ.append(a[i]+a[j]+a[j+1])
# for i in summ:
#     r.append(x-i)
# rs = min(r)
# print(rs+x)

