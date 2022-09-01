def LargeSmallSum(arr):
    arr.sort()
    even = []
    odd = []
    for i in range(len(arr)):
        if i%2!=0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    return even[len(even)-2]+odd[1]
print(LargeSmallSum([3,2,1,7,5,4]))