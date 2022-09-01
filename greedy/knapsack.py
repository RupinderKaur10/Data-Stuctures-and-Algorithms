class KnapsackPackage(object):
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight
    def __lt__(self, other):
        return self.cost < other.cost
class FractionalKnapsack(object):
    def knapsackResult(self, W, V, C, n):
        pack = []
        for i in range(n):
            pack.append(KnapsackPackage(W[i],V[i]))
        pack.sort(reverse=True)
        remain = C
        result = 0
        i = 0
        stop = False
        while stop != True:
            if pack[i].weight <= remain:
                remain -= pack[i].weight
                result += pack[i].value
            print("Pack ", i, " - Weight ", pack[i].weight, " - Value ", pack[i].value)
            if pack[i].weight > remain:
                i += 1
            if i == n:
                stop = True
        print(result)
if __name__ == "__main__":
    W = [15, 10, 2, 4]
    V = [30, 25, 2, 6]
    M = 37
    n = 4

    proc = FractionalKnapsack()
    proc.knapsackResult(W, V, M, n)