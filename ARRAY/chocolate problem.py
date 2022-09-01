def chocolate(num, m):
    num.sort()
    b = []
    for i in range(len(num)-(m-1)):
        difference = num[i+m-1] - num[i]
        b.append(difference)
    print(b)
    return min(b)


num = [12, 4, 7, 9, 2, 23, 25, 41,
30, 40, 28, 42, 30, 44, 48,
43, 50]
print(chocolate(num,7))
