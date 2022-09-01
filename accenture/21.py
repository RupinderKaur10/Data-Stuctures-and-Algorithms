A=[1,3,5,2,2]
N = len(A)
tSum = 0
sum = 0
for i in range(N):
    tSum+=A[i]
for i in range(N):
    if sum == tSum-sum-A[i]:
        print(i+1)
    sum+=A[i]
print("-1")