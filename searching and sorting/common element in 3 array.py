a1 = [1,2,10,20,40,80]
a2 = [6,7,20,80,100]
a3 = [3,4,15,20,30,70,80,120]
result = []
for i in range(len(a1)):
    if a1[i] in a2 and a1[i] in a3:
        print(a1[i],end=" ")
