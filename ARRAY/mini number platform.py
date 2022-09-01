from heapq import *
arr = list(map(int,input().strip().split()))
dep = list(map(int,input().strip().split()))
q = []
for a,d in sorted(zip(arr,dep),key=lambda x:x[0]):
    if not q or a<=q[0]:
        heappush(q,d)
    else:
        heapreplace(q,d)
print(len(q))
# def binarySearch(array,low,high,n):
#     if high>=low:
#         mid = (high+low)//2
#         if array[mid] == n:
#             return 1
#         elif array[mid] > n:
#             return binarySearch(array,low,mid-1,n)
#         else:
#             return binarySearch(array,mid+1,high,n)
#     else:
#         return -1
#
# def railway(a,b):
#     count = 0
#     res = []
#     res = a+b
#     res.sort()
#     result = [0]*len(res)
#     for i in range(len(res)):
#         x = binarySearch(a,0,len(a)-1,res[i])
#         if x==1:
#             count+=1
#             result[i] = count
#         else:
#             count-=1
#             result[i] = count
#     return (result)
# print(railway(a,b))
