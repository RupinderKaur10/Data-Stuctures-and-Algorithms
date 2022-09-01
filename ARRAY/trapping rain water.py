def maxwater(nums):
    n = len(nums)
    left_max = [0]*n
    right_max = [0]*n
    water = 0

    left_max[0] = nums[0]
    right_max[n-1] = nums[n-1]

    for i in range(1,n):
        left_max[i] = max(left_max[i-1],nums[i])
    print(left_max)
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],nums[i])
    print(right_max)
    for i in range(0,n):
        water += min(left_max[i],right_max[i])-nums[i]
        print(water)
    return water

print(maxwater([0,1,0,2,1,0,1,3,2,1,2,1]))


