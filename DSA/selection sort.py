def selectionsort(a,n):

    for i in range(n):
        z = i
        print(i)
        for j in range(i+1,n):
            if a[z] > a[j]:
                z = j
        a[i], a[z] = a[z], a[i]

    return a
a = [1,2,3,4,5,6]
n = len(a)
result = selectionsort(a, n)
print(result)

