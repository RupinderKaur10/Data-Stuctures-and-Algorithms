 #1 create an array by removing n/3 elements
 #2 remove the element only to obtain max(sum of first half - sum of other half)
def Binary_add(a,n,low,high):
    mid = int((low+high)//2)


def disered_array():
    a = [1,2,3]
    n = len(a)
    eleRemove = int(n/3)
    LB = int(n-eleRemove)
    i = 0
    summ = []
    # print(summ)
    for i in range(n):
        if LB == 1:
            return f"not valid"
        if LB == 2:
            for j in range(i+1,n):
                summ.append(a[i]-a[j])
                return max(summ)
        else:

print(disered_array())
# import math
# def first_half(a,n):
#     eleRemove = n/3
#     if n%2!=0:
#         lim = math.ceil(n/2)
#     else:
#         lim = int(n/2)
#     b = []
#     numEle = int(n-eleRemove)
#     summ = [0]*int(numEle/2)
#     for i in range(0,lim):
#         for j in range(i+1,lim):
#             summ[i] = a[i]+a[j]
#     if lim == 2:
#         for i in range(0,lim):
#             b.append(a[i])
#         return b
#     else:
#         return max(summ)
#
# def second_half(a,n):
#     eleRemove = n/3
#     if n%2!=0:
#         lim = math.ceil(n/2)
#     else:
#         lim = int(n/2)
#     b = []
#     numEle = int(n-eleRemove)
#     summ = [0]*int(numEle/2)
#     for i in range(lim,n+1):
#         print(i)
#         for j in range(i+1,n):
#             print(j)
#             summ[i] = a[i]+a[j]
#     if lim == 2:
#         n = len(b)
#         for i in range(n):
#             b.append(a[i])
#         return b
#     else:
#         return min(summ)
# print(second_half([1,2,3],3))
# print(first_half([1,2,3],3))

