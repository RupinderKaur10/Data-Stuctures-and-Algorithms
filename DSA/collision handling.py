class HashTable:

    def __init__(self):
        self.max = 10
        self.A = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        index = h % self.max
        return index

    def set(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.A):
            # if len(element) == 2 and element[0] == key:
            #     self.A[h][index] = (key, value)
            #     found = True
            element_key,element_value = element
            if element_key == key:
                found = True
                break
        if found:
            self.A[index] = (key, value)
        else:
            self.A.append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.A[h]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.A[h]):
            if kv[0] == key:
                print("delete", index)
                del self.A[h][index]

    def printarray(self):
        n = len(self.A)
        for i in range(n):
            print(self.A[i])


if __name__ == "__main__":
    t = HashTable()
    t.set("march 6",310)
    # t["march 7"] = 420
    # t["march 8"] = 67
    # t["march 17"] = 634
    t.printarray()
