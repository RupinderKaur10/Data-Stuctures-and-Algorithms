def precedence(char):
    if char == "*" and char == "/":
        return 3
    elif char == "+" and char == "-":
        return 2
    else:
        return 0
a ='p-q-r/a'
s = []
i = []
j = []
n = len(j)
for x in a:
   s.append(x)
for x in s:
    if x not in ['+', "-", "/", "*"]:
        i.append(x)
    if x in['+',"-","/","*"]:
        j.append(x)
        if precedence(x) > precedence(j[len(j)-1]):
            j.append(x)

        else:
            p = j.pop()
            i.append(p)
print(i)
print(j)

# j = [1,2,3,4]
# n = len(j)
# print(j[len(j)-1])



# print(j)
#     if x not in ['+',"-","/","*"]:
#         i.append(x)
# print(i)







