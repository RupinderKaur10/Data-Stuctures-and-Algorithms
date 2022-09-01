a = []
n = int(input("enter the number of elements in array\n"))
for i in range(n):
    element = int(input(f"enter the array {i} element\n"))
    a.append(element)
a.sort()
print(a[0],a[n-1])

