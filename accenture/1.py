r = int(input())
unit = int(input())
n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)
food = r * unit
count = 0
number = 0
for i in range(n):
    if count<food:
        count+=a[i]
        number+=1
    else:
        break
print(number)