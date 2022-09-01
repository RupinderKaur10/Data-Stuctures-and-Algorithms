a = "abcaacdef"
count=0
ans = ""
for char in a:
    if char not in ans:
        ans+=char
        count = max(count,len(ans))
    else:
        ans = ans[ans.find(char)+1:]+char

print(count)