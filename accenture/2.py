s = str(input())
a = int(s[0])
for i in range(1,len(s),2):
    if s[i] == "A":
        a&=int(s[i+1])
    elif s[i] == "B":
        a|=int(s[i+1])
    else:
        a^=int(s[i+1])
print(a)
# i = 1
# while i<len(s):
#     if s[i] == "A":
#         a&=int(s[i+1])
#     elif s[i] == "B":
#         a|=int(s[i+1])
#     elif s[i] == "C":
#         a^=int(s[i+1])
#     i+=2
# print(a)