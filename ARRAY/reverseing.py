a = []
n = int(input("enter the number of elements in array\n"))
for i in range(n):
    element = int(input(f"enter the array {i} element\n"))
    a.append(element)
print(a)
def reverse(a):
    i = 0            # first item
    j = len(a)-1   # last item
    while i<j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1 
    return a

result = reverse(a)
print(f"this is revered array \n{result}")
