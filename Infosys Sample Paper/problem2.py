def heros(N,M,H,A):
    total_power = H*M
    count = 0
    for i in range(N):
        turn = 0
        while turn < 1:
            total_power = total_power-A[i]
            turn += 1
            if total_power<0:
                count+=1
    return count
print(heros(5,3,3,[1,2,3,1,1]))