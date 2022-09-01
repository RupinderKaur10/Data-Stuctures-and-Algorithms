import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.c = 1
        self.A = self._make_array(self.c)

    def _make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def compare(self, f, s):
        if self.n < f < 0:
            return Exception("Invalid Index")
        if self.n < s < 0:
            return Exception("Invalid Index")
        c = self.A[f] - self.A[s]
        return f"you spent {abs(c)} dollar more from previous month"

    def _resize(self, new_cap):
        b = self._make_array(new_cap)
        for k in range(self.n):
            b[k] = self.A[k]
        self.A = b
        self.c = new_cap

    def __getitem__(self, index):
        size = self.n
        if size < index < 0:
            return Exception("Invalid index")
        return self.A[index]

    def FTEA(self):
        return f" the result is {self.A[0] + self.A[1] + self.A[2]}"

    def findout(self, value):
        for i in self.A:
            if i == value:
                return f"yes"
            else:
                return f'no'

    def append(self, ele):
        if self.n == self.c:
            self._resize(2 * self.c)
        self.A[self.n] = ele
        self.n += 1

    def insertAt(self, item, index):

        if index < 0 or index > self.n:
            print("please enter appropriate index..")
            return

        if self.n == self.c:
            self._resize(2 * self.c)

        for i in range(self.n - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]

        self.A[index] = item
        self.n += 1
        # for i in range(self.n):
        #
        #     return (self.A[i])

    def array(self):
        for i in range(self.n):
            print(self.A[i])


arr = DynamicArray()
arr._make_array(6)
# arr.append(1)
arr.insertAt(2200, 0)
arr.insertAt(2350, 1)
arr.insertAt(2600, 2)
arr.insertAt(2130, 3)
arr.insertAt(2190, 4)

# arr.array()
print(arr.array())
print(arr.compare(0, 1))
print(arr.FTEA())
print(arr.append(1980))
print(arr.array())
print(arr.insertAt(1930, 3))
print(arr.array())
