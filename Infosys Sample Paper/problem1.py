E = 2
N = 3
A = [1,5,2]
def Exercise(A, N, E):
    A.sort(reverse=True)
    count = 0
    for i in range(0,N):
        minus2 = 0
        while(E>0 and minus2<2):
            E-=A[i]
            minus2+=1
            count+=1
        if (E<=0):
            return count
        else:
            return -1
print(Exercise(A, N, E))
