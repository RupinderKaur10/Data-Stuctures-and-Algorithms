nums = [2,7,6,1,4,5]
best_sum = nums[0]
current_sum = 0
for i in range(len(nums)):
    current_sum += nums[i]
    if best_sum < current_sum:
        best_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print(best_sum)

