no_of_charm = 256
def badCharHeuristic(a, n):
    badChar = [-1] * no_of_charm
    for i in range(n):
        badChar[ord(a[i])] = i
    return badChar
def search(text, pattern):
    p = len(pattern)
    t = len(text)
    badChar = badCharHeuristic(pattern, p)
    s = 0
    while s <= (t - p):
        j = p - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print("pattern occur at shift = {}".format(s))
            s += (p - badChar[ord(text[s + p])] if s + p < t else 1)
            # if s+p<t:
            #     s+=p-badChar[ord(text[s+p])]
            # else:
            #     s+=1
        else:
            s += max(1, j - badChar[ord(text[s + j])])
