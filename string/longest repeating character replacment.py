# no_of_char = 256
# def dulpicate(a,count):
#     for i in a:
#         count[ord(i)] += 1
#     return count
# def changing(a,k):
#     r = []
#     count = [0]*no_of_char
#     count = dulpicate(a,count)
#     for i in count:
#         if i!=0:
#             r.append(i)
#     m = min(r)
#     b = abs(m-k)
#     if b == 0:
#         return len(a)
#     else:
#         return len(a)-m
# print(changing("bbabb",1))
"""2nd solution"""
# def findLen(a,k,ch):
#     n = len(a)
#     maxlen = 1
#     count = 0
#     l = 0
#     r = 0
#     while r<n:
#         if a[r]!=ch:
#             count+=1
#         while count>k:
#             if a[l]!=ch:
#                 count-=1
#             l+=1
#         maxlen = max(maxlen,r-l+1)
#         r+=1
#     return maxlen
#
# def answer(a,n,k):
#     maxlen = 1
#     for i in range(26):
#         maxlen = max(maxlen,)
"""3rd solution"""
def charReplacement(s,k):
    count = {}
    res = 0

    l=0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1+count.get(s[r],0)
        maxf = max(maxf,count[s[r]])

        while (r-l+1)-maxf>k:
            count[s[l]]-=1
            l+=1
        res = max(res,r-l+1)
    return res



