def bs(a, low, high, n):
	if high >= low:
		mid = high+low//2
		if mid == n:
			return mid
		elif mid > n:
			return bs(a, low, mid-1, n)
		else:
			return bs(a, mid+1, high, n)
	else:
		return -1
a = []
n = int(input("enter the number of elements:\n"))
for i in range(0,n):
	e = int(input("enter the elements you want in list:\n"))
	a.append(e)
print(a)
x = int(input("enter the index whose number you wants to find"))
n = a[x]
result = bs(a, 0, len(a)-1, n)

if result != -1:
	print("the element's index is", str(result))
else:
	print("the element is not present")



