a = [2,4,1,3,5]
n = len(a)
count=0
l = 0
r = 1
A = True
while A:
    if l >= len(a) or r >= len(a):
        l,r = 0,1
    if a[l]>a[r]:
        a[l],a[r] = a[r],a[l]
        count+=1
    l+=1
    r+=1
    b = a.sort()
    if a == b:
        A = False

print(count)
# count = 0
# i = 0
# while i<n-1:
#     for j in range(n-1):
#         if a[j]<a[j+1]:
#             break
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
#             count += 1
#     i+=1
# print(a,count)
