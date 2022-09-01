def bubblesort(a,n):

    issorted = 0
    for i in range(n):
        print(i+1, "number of pases")
        issorted = 1
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                print("no.of swaps",j)
                s = a[j]
                a[j] = a[j + 1]
                a[j + 1] = s
                issorted = 0
        if (issorted):
            return a

    # return a


