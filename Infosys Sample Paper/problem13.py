d = int(input("number the value"))
arr = [7,8,5,5,9,2,2,0,1,6]
res = arr[:d][::-1]+arr[d:][::-1]
ans = 0
count = 0
for i in res:
    ans^=i
    count+=ans
print(count)
