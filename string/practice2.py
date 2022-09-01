def sum(N,M):
    num = [1,2,3,4,5,6,7,8,9]
    summ =0
    if N == M:
        summ = 2
        return summ
    if N>M and N%M==0:
        m = M//M
        n = N//M
        summ = n+m
    if N<M and M%N==0:
        m = M//N
        n = N//N
        summ = n+m
    if N>M and N%M!=0:
        summ = M+N
    if N<M and M%N!=0:
        summ = M+N
    return summ
print(sum(5,6))
