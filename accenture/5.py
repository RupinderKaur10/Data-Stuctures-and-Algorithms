def differenceSum(n,m):
    result1 = 0
    result2 = 0
    for i in range(1,m+1):
        if i%n != 0 :
            result1+=i
            continue
        elif i%n == 0:
            result2+=i
            continue
    return abs(result1-result2)
print(differenceSum(4,20))