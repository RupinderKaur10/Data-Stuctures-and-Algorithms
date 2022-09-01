a = "b"
b = "d"
no_of_char = 256
def anagram(a,b):
    ah = [0]*no_of_char
    bh = [0]*no_of_char

    # for i in a:
    #     ah[i] = 0
    #     # ah[i]+=1
    for i in a:
        ah[ord(i)]+=1
    # for i in b:
    #     bh[i] = 0
    for i in b:
        bh[ord(i)]+=1
    if len(a)!=len(b):
        return "NO"
    for i in range(no_of_char):
        if ah[i]!=bh[i]:
            return "NO"
    return "YES"
    # if ah==bh:
    #     return "YES"
    # return "NO"
print(anagram(a,b))
# class data(object):
#     def __init__(self,s,index):
#         self.s = s
#         self.index = index
# def createDupArray(s,size):
#     dupArray = []
#     for i in range(size):
#         dupArray.append(data(s[i],i))
#     return dupArray
#
# def groupAnagrams(wordarray,size):
#     dupArray = createDupArray(wordarray,size)
#     for i in range(size):
#         dupArray[i].s = "".join(sorted(dupArray[i].s))
#     dupArray = sorted(dupArray,key=lambda k:k.s)
#     for word in dupArray:
#         return wordarray[word.index]
# wordArr = ["eat","tea","tan","ate","nat","bat"]
# size = len(wordArr)
# print(groupAnagrams(wordArr, size))
# import collections
#
#
# def groupAnagrams(s):
#     ans = collections.defaultdict(list)
#     for i in s:
#         ans[tuple(sorted(s))].append(s)
#     return ans.values()
# wordArr = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(wordArr))
