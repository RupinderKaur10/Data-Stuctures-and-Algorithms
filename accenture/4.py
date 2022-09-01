
def absolute(arr,num,diff):
    count = 0
    for i in range(len(arr)):
        if diff >= abs(arr[i]-num):
            count+=1
    if count>0:
        return count
    else:
        return -1
arr = [12, 3, 14, 56, 77, 13]
num = 13
diff = 2
print(absolute(arr,num,diff))
