a = [2,4,6,8,9,3,1,7]

def swap(a,ind1,ind2):
    temp = a[ind1]
    a[ind1] = a[ind2]
    a[ind2] = temp
count = 0
for i in range(len(a)-1):
    if a[i] % 2 != 0:
        if a[i+1]%2!=0:
            continue
        swap(a, i, i + 1)
        print(a)
        count += 1
    for j in range(len(a)-1,i+1,-1):
        if a[j]%2==0:
            if a[j-1]%2==0:
                continue
            swap(a,j,j-1)
            print(a)
            count+=1
print(count)
# count = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         continue
#     else:
#         for j in range(i+1,len(a)):
#             print(a)
#             if a[j]%2==0:
#                 swap(a,i,j)
#                 count += 1
#                 # print(a)
#                 break
# print(count)
