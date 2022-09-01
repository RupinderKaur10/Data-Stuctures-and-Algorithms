class data(object):
    def __init__(self, m, b):
        self.m = m
        self.b = b
    def __lt__(self, other):
        return self.m < other.m
class monster(object):
    def defeatResult(self, n, e, m, b):
        pack = []
        for i in range(n):
            pack.append(data(m[i], b[i]))
        pack.sort()
        count = 0
        for i in range(n):
            if pack[i].m <= e:
                e += pack[i].b
                count += 1
        return count
if __name__ == "__main__":
    n = 5
    e = 100
    m = [101, 100, 304, 199, 99]
    b = [100, 1, 542, 10, 0]
    NumMon = monster()
    print(NumMon.defeatResult(n, e, m, b))
