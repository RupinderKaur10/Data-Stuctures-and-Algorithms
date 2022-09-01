a =[142, 112, 54, 69, 148, 45, 63 ,158, 38, 60 ,124, 142, 130, 179, 117, 36, 191, 43, 89 ,107, 41, 143, 65, 49 ,47, 6, 91, 130, 171, 151, 7 ,102, 194 ,149, 30, 24, 85, 155 ,157, 41 ,167, 177, 132, 109, 145, 40, 27, 124 ,138 ,139 ,119, 83, 130, 142, 34, 116, 40, 59 ,105, 131, 178, 107, 74, 187 ,22 ,146, 125, 73 ,71, 30 ,178, 174, 98 ,113]
n = len(a)
k = 254
summ = 0
l = 0
r = 0
if summ == k:
    print(l+1,r+1)
while r<n:
    summ+=a[r]
    # if summ+a[r+1]<=k:
    #     summ+=a[r+1]
    #     r+=1
    while summ>k and l>r:
        summ-=a[l]
        l+=1
    if summ == k:
        print(l+1,r+1)
        break
    r+=1
print(-1)
# for i in range(len(a)):
#     res = a[i]
#     for j in range(i+1,len(a)):
#         if res == k:
#             print(i+1,j)
#             break
#         if res>k:
#             break
#         res+=a[j]



