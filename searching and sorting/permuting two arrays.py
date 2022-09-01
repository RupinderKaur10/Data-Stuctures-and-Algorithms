#with BUG

class data(object):
    def __init__(self,A,B):
        self.A = A
        self.B = B

class permutation(object):

    def permuting(self, a, b, k):
        pack = []
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] + b[j] >= k:
                    pack.append(data(a[i],b[j]))
        if len(pack) >= len(a):
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    A = [1,2,2,1]
    B = [3,3,3,4]
    result = permutation()
    print(result.permuting(A,B,5))
