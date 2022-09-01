def findMinSum(a, b, n):
    # Sort both arrays
    a.sort()
    b.sort()

    # Find sum of absolute differences
    sum = 0

    for i in range(n):
        sum = sum + abs(a[i] - b[i])

    return sum


a = [3,2,1]
b = [2,1,3]
n = len(a)

print(findMinSum(a, b, n))