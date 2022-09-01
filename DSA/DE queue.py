import ctypes


class dynamicqueue(object):

    def __init__(self, cap):
        self.c = cap
        self.f = -1  # first element's index
        self.b = -1  # last element's index
        self.n = 0  # size of array
        self.A = self._make_array(self.c)

    def _make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def enqueueR(self, items):
        if self.n == self.c:
            return f"queue is full at rare end"
        self.A[self.n] = items
        self.b += 1
        self.n += 1

    def enqueueF(self, items):
        if self.f == -1:
            return f"queue is full from front {self.f}"
        self.A[self.f] = items
        self.f -= 1

    def dequeueF(self):
        if self.f == self.b:
            return f"queue is empty"
        for i in range(self.n):
            if i == self.f + 1:
                self.A[i] = None
        self.f += 1

    def dequeueR(self):
        self.A[self.n] = None
        self.b -= 1

    def peek(self, index):
        if self.n < index < 0:
            return f"Invalid Index"
        for i in range(self.n):
            if i == index:
                return self.A[i]

    def printqueue(self):
        for i in range(self.n):
            print(self.A[i])

    def isempty(self):
        if self.n == 0:
            return f"queue is empty"
        elif self.n == self.c:
            return f"queue is full"
        else:
            return f"queue has {self.n} elements"

    def front(self):
        return self.f

    def end(self):
        return self.b


q = dynamicqueue(8)
q.enqueueR(3)
q.enqueueR(4)
q.enqueueR(2)
q.enqueueR(9)
q.enqueueR(1)
q.dequeueF()
q.dequeueF()
print(q.front())
q.enqueueF(7)
print(q.front())
print(q.printqueue())
