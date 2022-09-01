class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, item):
        mid = self.data
        if item == mid:
            return f"{mid} is present in Tree"
        elif item < mid:
            if self.left is None:
                return f"{item} is not present in Tree"
            return self.left.search(item)
        elif item > mid:
            if self.right is None:
                return f"{item} is not present in Tree"
            return self.right.search(item)
        else:
            return f"{item} is not present in Tree"

    # def deleteEle(self, item):
    #     if item < self.data:
    #         if self.left:
    #             self.left.deleteEle(item)
    #
    #     elif item > self.data:
    #         if self.right:
    #             self.right.deleteEle(item)
    #
    #     elif item == self.data:
    #         if self.left is None and self.right is None:
    #             return None
    #         if self.left is None:
    #             return self.right
    #         if self.right is None:
    #             return self.left
    #
    #         min_value = self.right.minvalue()
    #         self.data = min_value
    #         self.right = self.right.deleteEle(min_value)
    #     return self
    #
    # def minvalue(self):
    #     if self.left is None:
    #         return self.data
    #     return self.left.minvalue()
    #
    # def maxvalue(self):
    #     if self.right is None:
    #         return self.data
    #     return self.right.maxvalue()
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def display(self):
        # in order traversal
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()
        # pre order traversal
        # print(self.data)
        # if self.left:
        #     self.left.display()
        # if self.right:
        #     self.right.display()
        # post order traversal
        # if self.left:
        #     self.left.display()
        # if self.right:
        #     self.right.display()
        # print(self.data)


root = Node(6)
root.insert(8)
root.insert(9)
root.insert(2)
root.insert(1)
root.insert(3)
# root.insert(3)
root.insert(7)
# root.display()
# print(root.search(7))
root.delete(7)
root.display()
