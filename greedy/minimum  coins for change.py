
def MinCoin(coins,value):
    small = []
    for i in range(len(coins)):
        if coins[i]<=value:
            small.append(coins[i])
    small.sort(reverse=True)
    res = 0
    i=0
    stop = True
    while stop:
        if small[i]<=value:
            diff = value-small[i]
            res+=1
            value = diff
            continue
        else:
            i+=1
        if diff == 0:
            stop = False

    return res
if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    value = int(input("enter the value"))
    print(MinCoin(coins,value))