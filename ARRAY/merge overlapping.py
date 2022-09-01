arr=[[6, 8], [1, 9], [2, 4], [4, 7]]


def mergeIntervals(arr):
    arr.sort(key=lambda x: x[0])
    print(arr)

    index = 0
    for i in range(1, len(arr)):

        if (arr[index][1] >= arr[i][0]):
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]

    print("The Merged Intervals are :", end=" ")
    for i in range(index + 1):
        print(arr[i], end=" ")

mergeIntervals(arr)

