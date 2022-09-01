class data(object):
    def __init__(self, R, T):
        self.R = R
        self.T = T
    def __lt__(self, other):
        return self.R < other.R
class jobSequencing(object):
    def jobseqResult(self, R, T, n):
        pack = []
        for i in range(n):
            pack.append(data(R[i], T[i]))
        pack.sort(reverse=True)
        for i in range(n):
            print(pack[i].T,pack[i].R)
        m = max(T)
        slot = [0]*(m)
        for i in range(m):
            for j in range(i,n):
                if i<pack[j].T and slot[i] == 0:
                    slot[i] = pack[j].R

        finalRes = 0
        for i in range(len(slot)):
            finalRes = finalRes+slot[i]

        return f"Maximum Profit is {finalRes} and the Sequence of job is {slot}"
R = [20,15,10,5,1]
T = [2,2,1,3,3]
n = len(R)
result = jobSequencing()
print(result.jobseqResult(R,T,n))
