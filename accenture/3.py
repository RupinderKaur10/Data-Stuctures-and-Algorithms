# at least 4 character
# at least one numeric but on first index
# at least one capital letter
# must not have space and /
s = "aA1_67"
# digit = "1234567890"
# capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# char = "/ "
def password(s,n):
    if n<4 or s[0].isdigit():
        return "0"
    cap = 0
    num = 0
    for i in range(n):
        if s[i]==' ' or s[i]=='/':
            return 0
        if s[i]>='A' and s[i]<='Z':
            cap+=1
        elif s[i].isdigit():
            num+=1
    if cap>0 and num>0:
        return 1
    else:
        return 0
    # for i in range(len(s)):
    #     if len(s) < 4 or s[0].isdigit():
    #         return "0"
    #     if s[i]==" " or s[i] == "/":
    #         return "0"
    #     elif s[i].isdigit():
    #         continue
    #     elif s[i] in capital:
    #         continue
    #     return "1"
print(password(s,len(s)))

