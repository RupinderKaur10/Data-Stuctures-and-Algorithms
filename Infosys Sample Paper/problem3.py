a = [1,2,3,4,5]
n = len(a)
def slope(a,n,low,high):
    mid = low+high//2
    if n%2 != 0:
        count = 0
        for i in range(1,mid+1):
            if a[mid+i] != a[mid]-i:
                a[mid+i] = a[mid]-i
                count+=1
                if a[mid-i] != a[mid]-i:
                    a[mid-i] = a[mid]-i
                    count+=1
            else:
                continue
    else:
        count = 0
        for i in range(1,mid):
            if a[mid+i] != a[mid]-i:
                a[mid+i] = a[mid]-i
                count+=1
                if a[mid-(i+1)] != a[mid]-i:
                    a[mid-(i+1)] = a[mid]-i
                    count+=1
    return count

print(slope(a,n,0,len(a)))
