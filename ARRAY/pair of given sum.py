def printPairs(arr, arr_size, sum):
    hashmap = {}
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp in hashmap):
            print(f'Pair with given sum {sum} is ({temp},{arr[i]}) at indices ({hashmap[temp]},{i})')
        hashmap[arr[i]] = i
# driver code
A = [-1,0,1,2,-1,-4]
n = 0
printPairs(A, len(A), n)