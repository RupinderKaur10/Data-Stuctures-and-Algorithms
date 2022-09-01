def checkDuplicate(num):
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num) - 1):
            if num[i] == num[j]:
                return True
    return False

num = [4,9,6,2,8,7]
print(checkDuplicate(num))