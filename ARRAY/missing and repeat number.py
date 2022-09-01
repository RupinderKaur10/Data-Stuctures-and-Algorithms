
A = [2,2]

def repeatNumber(A):
    repeat = sum(A)-sum(set(A))
    n = len(A)
    sum_n = int((n*(n+1))/2)
    missing = sum_n-sum(set(A))
    return [repeat,missing]
print(repeatNumber(A))