def longestSubArrWithSumDivByK(a,k):
    n = len(a)
    um = {}
    max_len = 0
    cur_sum = 0
    for i in range(n):
        cur_sum+=a[i]
        mod = ((cur_sum%k)+k)%k
        if mod == 0:
            max_len = i+1
        elif mod in um.keys():
            if max_len<(i-um[mod]):
                max_len = i-um[mod]
        else:
            um[mod]=i
    return max_len
a = [2,7,6,1,4,5]
k =3
print(longestSubArrWithSumDivByK(a,k))
