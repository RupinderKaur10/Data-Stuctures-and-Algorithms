def check(i):
    s = str(i)
    x = 0
    y = len(s) - 1
    while y > 0:
        if s[x] != s[y]:
            break
        else:
            return i
        x += 1
        y -= 1


def plaindrome(a, b):
    res = []
    for i in range(a, b):
        temp = check(i)
        res.append(temp)
    for i in res:
        if i is not None:
            print(i, end=" ")


plaindrome(10, 80)
