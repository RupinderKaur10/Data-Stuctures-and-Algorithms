def Matix(n,arr):
    even = []
    odd = []
    for i in range(n):
        if i%2==0:
            even.append(arr[i])
        else: odd.append(arr[i])
    even.sort()
    odd.sort()
    return even[len(even)-2]+odd[len(odd)-2]
print(Matix(5,[3,4,1,7,9]))