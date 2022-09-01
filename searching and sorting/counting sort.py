def count_sort(a):
    max_ele = int(max(a))
    min_ele = int(min(a))
    range_of_ele = max_ele-min_ele+1

    count_a = [0 for _ in range(range_of_ele)]
    output_a = [0 for _ in range (len(a))]

    for i in range(0,len(a)):
        count_a[a[i]-min_ele]+=1
    for i in range(1,len(count_a)):
        count_a[i]+=count_a[i-1]
    for i in range(len(a)-1,-1,-1):
        output_a[count_a[a[i]-min_ele]-1]=a[i]
        count_a[a[i]-min_ele]-=1
    for i in range(0,len(a)):
        a[i] = output_a[i]
    return a
print(count_sort([4,4,7,2,9,9,3,6,8]))