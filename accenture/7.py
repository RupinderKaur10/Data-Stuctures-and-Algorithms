def ProductSmallestPair(sum,arr):
    arr.sort()
    summ = arr[0]+arr[1]
    if summ<=sum:
        result = arr[0]*arr[1]
        return result
    if len(arr)<2 or len(arr) == 0:
        return -1
    return -1
print(ProductSmallestPair(4,[9,8,3,-7,3,9]))
