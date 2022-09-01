s = "hello"
r = {}
for i in s:
    if i in r:
        print(i)
        break
    r[i] = 0

