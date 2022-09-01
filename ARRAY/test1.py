a = [1,2,3,4,5,6]
n = len(a)
# m = a[0]
m = max(a)+min(a)
# for i in range(n):
#     m = max(m,a[i])
    # m = a[i]
left = 0
right = n-1
flag = True
while left<n and right>0:
    for i in range(n):
        if flag:
            val = a[right]%m
            a[i]+=m*val
        else:
            val = a[left]%m
            a[i]+=m*val
        left += 1
        right -= 1
        flag = False

for i in range(n):
    a[i] = a[i]//m
print(a)
# res = []
# res.append(a[n-1])
# j = n-1
# while j>0:
#     i = n-j-1
#     if a[j] not in res:
#         res.append(a[j])
#     if a[i] not in res:
#         res.append(a[i])
#     j-=1
