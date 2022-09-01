s = "move-hyphen-to-front"
# h = []
# l = []
# for i in range(len(s)):
#     if s[i] =="-":
#         h.append(s[i])
#     else: l.append(s[i])
# for i in range(len(h)):
#     print(h[i],end="")
# for i in range(len(l)):
#     print(l[i],end="")
count = 0
final = ""
for i in s:
    if i == "-":
        count+=1
    else: final+=i
print("-"*count,final)
