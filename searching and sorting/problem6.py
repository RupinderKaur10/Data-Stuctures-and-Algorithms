a = [1,2,8,10,10,12,19]
x = int(input("enter x"))
for i in range(len(a)):
    if a[i] == x:
        print("floor is :",a[i])
        break
    if a[i] >= x:
        print("ceil is :",a[i])
        break

