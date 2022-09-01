#will solve it later
nums = [3,-1,4]
def product(nums):
    res = max(nums)
    curMin, curMax = 1,1

    for n in nums:
        temp = curMax*n
        curMax = max(n,n*curMin,n*curMax)
        curMin = min(n,n*curMin,temp)
        res = max(res,curMax)
    return res
print(product(nums))