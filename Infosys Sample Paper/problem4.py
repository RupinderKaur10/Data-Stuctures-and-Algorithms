a = [3,3]
n = len(a)
count = 0
for i in range(0,n-1):
    if a[i] <= a[i+1]:
        a[i] = a[i]-i
        count+=1
        continue
else:
    print(count)
# print(count)