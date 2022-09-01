def Calculate(m,n):
    count=0
    for i in range(m,n):
        if i%3==0 and i%5==0:
            count+=i
    return count
print(Calculate(100,160))