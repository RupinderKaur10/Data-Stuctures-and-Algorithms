def ReplaceCharacter(s,ch1,ch2):
    a = []
    for i in range(len(s)):
        a.append(s[i])
    for i in range(len(a)):
        if a[i] == ch2:
            a[i] = ch1
        elif a[i] == ch1:
            a[i] = ch2
    for i in range(len(a)):
        print(a[i],end="")
ReplaceCharacter("apples","a","p")