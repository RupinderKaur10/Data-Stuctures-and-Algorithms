def password(S):
    u = 0
    l = 0
    d = 0
    for i in range(len(S)):
        if S[i].islower():
            l += 1
        if S[i].isupper():
            u += 1
        if S[i].isdigit():
            d += 1
        continue
    if u == 0 or l == 0 or d == 0:
        return "NO"
    else:
        return "YES"


T = int(input())

while T != 0:
    S = str(input())
    res = password(S)
    print(res)
    T -= 1
