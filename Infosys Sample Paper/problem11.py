n = str(input("number"))
d = str(input("digit"))
res = []
for i in range(len(n)-1):
    if n[i]==d:
        temp= n[0:i]+n[i+1:]
        res.append(temp)
print(str(max(res)))