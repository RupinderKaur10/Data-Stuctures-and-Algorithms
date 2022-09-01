class HashTable:

    def __init__(self):
        self.max = 100
        self.A = ([] for i in range(self.max))

    def get_hash(self,key):
        h = 0
        for i in key:
            h+=ord(i)
        index = h%self.max
        return index

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.A[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.A[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.A[h] = None


if __name__=="__main__":
    h = HashTable
    # h["apple"] = 2
    # h["orange"] = 10
    # h["mango"] = 4
    # h["banana"] = 6
    # h["watermelon"] = 3

