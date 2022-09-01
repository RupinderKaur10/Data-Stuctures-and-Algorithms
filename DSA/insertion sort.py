def insertionsort(a, n):
    for i in range(n):
        key = a[i]
        j = i - 1
        print(i)
        while j >= 0 and a[j] > key:
            # a[j] = key
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
a = [1,2,3,4,5]
n = len(a)
result = insertionsort(a,n)
print(result)