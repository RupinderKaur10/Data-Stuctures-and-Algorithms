def bS(a, n):
	high = len(a) - 1
	low = 0
	mid = 0
	while low<=high:
		mid = (high+low)//2
		if mid > n :
			high = mid-1
		elif mid < n:
			high = mid+1
		else:
			return mid

	return -1

a = []
n = int(input("enter the number of elements:\n"))
for i in range(0,n):
	e = int(input("enter the elements you want in list:\n"))
	a.append(e)
print(a)
x = int(input("enter the index whose number you wants to find"))
n = a[x]
result = bS(a, n)

if result != -1:
	print("the element's index is", str(result))
else:
	print("the element is not present")

