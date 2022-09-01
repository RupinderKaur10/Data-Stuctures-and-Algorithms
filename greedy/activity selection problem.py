class data(object):

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __lt__(self, other):
        return self.finish < other.finish

class activitySelection(object):
    @staticmethod
    def linkingResult(S, F):
        pack = []
        for i in range(len(S)):
            pack.append(data(S[i], F[i]))
        pack.sort()
        res = [None]*len(S)
        res[0] = 0
        for i in range(1,len(S)-1):
            if pack[i-1].start <= pack[i].start:
                res[i] = i
        return res
if __name__ == "__main__":
    S = [1, 3, 0, 5, 8, 5]
    F = [2, 4, 6, 7, 9, 9]
    n = len(S)
    result = activitySelection
    print(result.linkingResult(S, F))
