a = [2, 7, 6, 1, 4, 5]
k = 3
# n = len(a)
# r = []
# summ = 0
# for i in range(n):
#     for j in range(i+1,n):
#         summ+=a[j]
#         if summ%k==0:
#             summ = 0
#             r.append(j)
# print(r)

def MaxLen(a):
    hash_map = {}
    max_len = 0
    curr_sum = 0
    for i in range(len(a)):
        curr_sum+=a[i]
        if a[i]==0 and max_len==0:
            max_len = 1
        if curr_sum == 0:
            max_len = i+1
        if curr_sum in hash_map:
            max_len = max(max_len,i-hash_map[curr_sum])
            print(i-hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
    return max_len,hash_map
print(MaxLen(a))




