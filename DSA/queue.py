import ctypes


# import objects


class dynamicqueue(object):

    def __init__(self, cap):
        self.c = cap
        self.f = -1  # first element's index
        self.b = -1  # last element's index
        self.n = 0  # size of array
        self.A = self._make_array(self.c)

    def _make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def enqueue(self, items):
        # if self.n == self.c:
        #     return self._resize(2 * self.c)
        self.A[self.n] = items
        self.b += 1
        self.n += 1

    # def _resize(self, new_cap):
    #     ba = self._make_array(new_cap)
    #
    #     for i in range(self.n):
    #         ba[i] = self.A[i]
    #
    #     self.A = ba
    #     self.c = new_cap

    def dequeue(self):
        for i in range(self.n):
            if i == self.f+1:
                self.A[i] = None
        # for i in range(self.n):
        #     self.A[i] = self.A[i - 1]
        self.f += 1

    def front(self):
        return self.f

    def end(self):
        return self.b

    def printqueue(self):
        for i in range(self.n):
            print(self.A[i])

    def peek(self,index):
        if self.n<index<0:
            return f"Invalid Index"
        for i in range(self.n):
            if i == index:
                return self.A[i]

    def isempty(self):
        if self.n == 0:
            return f"queue is empty"
        elif self.n == self.c:
            return f"queue is full"
        else:
            return f"queue has {self.n} elements"

q = dynamicqueue(7)
# print(q.end())
q.enqueue(2)
# # print(q.end())
q.enqueue(3)
# # print(q.end())
q.enqueue(5)
# # print(q.end())
q.enqueue(1)
# # print(q.end())
q.enqueue(6)
# # print(q.end())
q.enqueue(9)
q.enqueue(4)
# # print(q.end())
# print(q.printqueue())
# # print(q.front())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())

print(q.printqueue())
print(q.front())
# print(q.end())
print(q.peek(1))
print(q.isempty())
