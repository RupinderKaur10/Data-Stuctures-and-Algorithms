n = int(input("enter the number of element"))
a = [0]*(n+5)
a[0] = 0
a[1] = 1
for i in range(1,n-3):
    a[i*2] = a[i]
    a[(i*2)+1] = a[i]+a[i+1]
print(max(a))