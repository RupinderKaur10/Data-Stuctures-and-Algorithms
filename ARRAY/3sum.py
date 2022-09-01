arr = [0,-1,1]
dup = []
result = []
n = len(dup)
def pair(arr):
    arr.sort()
    for i, a in enumerate(arr):
        if i >0 and a == arr[i-1]:
            continue
        l, r = i + 1, len(arr) - 1
        while l < r:
            threesum = a + arr[l] + arr[r]
            print(threesum)
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                result.append([a,arr[l],arr[r]])
                l+=1
                while arr[l] == arr[l-1] and l<r:
                    l+=1

    return result

print(pair(arr))
