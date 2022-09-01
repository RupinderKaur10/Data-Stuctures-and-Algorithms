a = [6202,4625,5469,2038,5916,3405,5533,7004,2469,9853,4992,361,9819,3294,7195,4036,9404,8767,5404,1711,3214,3100,3751,2139,5437,4993,1759,9572,6270,3789,9623,2472,9493]
flag = True
for i in range(len(a)-1):
    if flag is True:
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    else:
        if a[i]<a[i+1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    flag = bool(1-flag)
print(a)
# l = 0
# r = 1
# loop = True
# while loop:
#     if a[l]>a[r]:
#         a[l],a[r] = a[r],a[l]
#         l+=2
#     if l>len(a)-3 or r>len(a)-3:
#         loop = False
#     elif a[r]>a[l]:
#         r+=2

# print(a)