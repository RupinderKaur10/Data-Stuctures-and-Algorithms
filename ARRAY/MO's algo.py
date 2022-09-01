import math

def queryResult(a,q):

    q.sort(key=lambda x: x[1])
    cl,cr,cs = 0,0,0

    for i in range(len(q)):
        l,r = q[i]
        # Remove extra elements from previous range
        # if previous range is [0, 3] and current
        # range is [2, 5], then a[0] and a[1] are subtracted
        while cr<l:
            cs-=a[cl]
            cl+=1
        # Remove elements of previous range
        # when previous range is [0, 10] and current range
        # is [3, 8], then a[9] and a[10] are subtracted
        while cr>r+1:
            cs-=a[cr-1]
            cr-=1
        # Add elements of current range
        while cl>l:
            cs+=a[cl-1]
            cl-=1
        while cr<=r:
            cs+=a[cr]
            cr+=1
        print("sum of",q[i],"is",cs)

