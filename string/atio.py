def atio(s):
    res = 0
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i += 1
    for j in range(i,len(s)):
        if s[j].isalpha():
            return 0
        res = res * 10 + (ord(s[j]) - ord('0'))
    return sign*res
print(atio("123"))