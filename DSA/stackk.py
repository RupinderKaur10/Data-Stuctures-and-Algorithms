import ctypes


class stackusingarray():

    def __init__(self):
        self.b = None
        self.n = -1  # size of array
        self.c = 8  # capacity of array
        # self.t = 0
        self.a = self._make_array(self.c)

    def _make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def push(self, ele):
        if self.n == self.c:
            return f"stak is full"
        self.a[self.n] = ele
        self.n += 1
        # return self.n
        # self.t+=1

    # def _resize(self, new_cap):
    #     b = self._make_array(new_cap)
    #     for i in range(self.n):
    #         b[i] = self.a[i]
    #     self.a = b
    #     self.c = new_cap

    def pop(self):
        if self.n == 0:
            return f"stack is empty"
        self.a[self.n - 1] = 0
        self.n -= 1

    def trav(self):
        for i in range(self.n):
            r = self.a[i]
            print(r)

    def peek(self, index):
        if self.n < index < 0:
            return f"index out of bound"
        for i in range(self.n):
            if i == index:
                return self.a[i]

    def isEmpty(self):
        # i = 0
        if self.n <= self.c:
            # self.a[self.n] = None
            print("stack is empty")
        else:
            print("stack is full")



    def bracketmatching(self, arr):
        stack = []
        b =[]
        for i in range(len(arr)):
            b.append(arr[i])

        for i in b:
            if i in ["(", "[", "{"]:
                stack.append(i)
            print(stack)

            if not stack:
                return False

            char_popped = stack.pop()
            if char_popped == "(":
                if i != ")":
                    return False
            if char_popped == "[":
                if i != "]":
                    return False
            if char_popped == "{":
                if i != "}":
                    return False

        if stack:
            return False
        else:
            return True

    # def isfull(self):
    #     if self.n == self.c:
    #         print("stack is full")


re = stackusingarray()
arr = "2*4(7*9)[]{}"
if re.bracketmatching(arr):
    print("balanced")
else:
    print("not balanced")


# b = []
# s = []
#
# for i in range(len(a)):
#     b.append(a[i])
# print(b)
# for i in range(len(b)):
#     if b[i] is '(' or "[" or '{':
#         s.append(b[i])

    # if b[i] == ')'  :
    #     s.pop()
    #
    # if b[i] == '[':
    #     s.append(b[i])
    #
    # if b[i] == ']':
    #     s.pop()
    #
    # if b[i] == '{':
    #     s.append(b[i])
    #
    # if b[i] == "}":
    #     s.pop()
# print(s)
# if not s:
#     print("the expression is balanced")
# else:
#     print("expression is not balanced")
