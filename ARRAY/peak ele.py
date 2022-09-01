def peakElement(arr, n):
    if n == 1:
        return n - 1
    for i in range(n):
        curr_elem = arr[i]
        if i == 0 and curr_elem > arr[i + 1]:
            return i
            break
        elif i == n - 1 and curr_elem > arr[i - 1]:
            return i
            break
        if i < n and curr_elem > arr[i + 1] and curr_elem > arr[i - 1]:
            return i
            break
    # for i in range(n-1):
    #     if a[i-1] < a[i] > a[i + 1] or a[n-1]>a[n-2]:
    #         return 1
    # else:
    #     return 0
a = list(map(int,input().strip().split()))
print(peakElement(a,len(a)))