prices = [100,180,260,310,40,535,695]
def maxProfit(prices):
    if not prices:
        return 0
    max_prof = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_prof = max(max_prof, prices[i] - min_price)
    print(min_price,prices[i])
    return max_prof
print(maxProfit(prices))