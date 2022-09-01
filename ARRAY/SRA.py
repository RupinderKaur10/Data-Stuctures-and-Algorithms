def rotate(a, k, target):
    n = len(a) - 1
    b = []
    for i in range(k, n + 1):
        b.append(a[i])
    for j in range(0, k):
        b.append(a[j])
    i = 0
    while i < len(b):
        if b[i] == target:
            return i
        i+=1
    return -1

a = [0, 1, 2, 4, 5, 6, 7]
k = 3
target = 0
print(rotate(a, k, target))
