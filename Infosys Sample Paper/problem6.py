
def sameNum():
    a = [1, 2]
    num = len(a)
    count = 0
    a.sort()
    while len(a)!=0:
        if a[0]!=a[-1]:
            a.remove(a[-1])
            a.remove(a[0])
            count += 1
        else:
            a.remove(a[0])
            count += 1
    print(count)
sameNum()