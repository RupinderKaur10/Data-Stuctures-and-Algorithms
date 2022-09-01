def FindAutoCorrect(n):
    res = []
    i=0
    while i<len(n):
        count = 0
        for j in n:
            if j == i:
                count+=1
        res.append(count)
        count = 0
        i+=1
    for i in range(len(n)):
        if res[i] != n[i]:
            break
        return 0
    if res[len(res)-1]!=0:
        return len(res)
    else: return len(res)-1
print(FindAutoCorrect("1210"))