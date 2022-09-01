import math as mt


def minCost(coin, k):
    coin.sort()
    n = len(coin)
    coins_needed = mt.ceil(n // (k + 1))
    res = 0
    for i in range(coins_needed):
        res = res + coin[i]
    return res


coin = [8, 5, 3, 10, 2, 7, 15, 25]
print(minCost(coin, 4))
