class data(object):
    def __init__(self, a, index):
        self.a = a
        self.index = index
    def __lt__(self, other):
       return self.a < other.a
class MaxInarr(object):
    def data(self, a):
        pack = []
        for i in range(len(a)):
            pack.append(data(a[i], i))
        pack.sort(reverse=True)
        print(pack[0].a, pack[0].index)


a = [23, 45, 82, 27, 66, 12, 78, 13, 71, 86]
MaxInarr.data(a,a)
