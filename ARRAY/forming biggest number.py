nums = [54, 546, 548, 60]
def biggestnumber(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]+nums[i]>nums[i]+nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    result="".join(nums)
    return result

print(biggestnumber(nums))