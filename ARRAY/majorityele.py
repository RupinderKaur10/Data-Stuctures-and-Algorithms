def majorityElement(A, N):
    count = {}
    for i in A:
        count[i] = 0
    for i in A:
        count[i] += 1
    for i in count:
        if max(count.values())>N//2:
            r = count.values()
        else:
            return -1
    for i in count:
        if count[i]==max(r):
            value = i
    # value = [i for i in count if count[i]==max(r)]
    return value
    # r = [i for i in count if count[i]==count.values()>len(A)//2 ]
    # return r
A = [3,1,3,3,2]
# A = list(map(int,input().strip().split()))
print(majorityElement(A,len(A)))