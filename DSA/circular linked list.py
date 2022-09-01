class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.last = None

    # INSERTION IN CIRCULAR LINKED LIST
    # FROM LAST ITEM
    def addtoempty(self, data):
        new_node = Node(data)
        if self.head is not None:
            return self.head
        self.head = new_node
        self.head.next = self.head
        return self.head

    def addtobegin(self, data):
        new_node = Node(data)
        if self.last is not None:
            return self.addtoempty(data)
        new_node.next = self.last.next
        self.last.next = new_node
        return self.last

    def addtoend(self, data):
        new_node = Node(data)
        if self.last is not None:
            return self.addtoempty(data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
        return self.last

    def addafter(self, data, item):
        new_node = Node(data)
        if self.head is None:
            return None
        p = self.head.next
        while p:
            if p is item:
                new_node.next = p.next
                p.next = new_node

                if p == self.head:
                    self.head = new_node
                    return self.head
                else:
                    return self.head
            p = p.next
            if p is self.head.next:
                return f"{item} is not in the list"

    # PRINTING CLL FROM HEAD ITSELF
    # def printlist(self):
    #     p = self.last.next
    #     while p:
    #         print(self.last)
    #         p = p.next
    #         if p == self.last.next:
    #             print("end")
    #             break
    def printList(self):

        temp = self.head

        if self.head is not None:
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break

    # INSERTION AT BEGINNING

    def push(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

        # new_node = Node(new_data)
        # new_node.next = self.last
        # self.last = new_node
        # print(self.last)

    def insertafter(self, prev_node, new_data):

        if prev_node is None:
            return f"please enter the node present in the list"
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # def append(self, new_data):
    #     new_node = Node(new_data)
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next
    #     temp.next = new_node
    # if temp.next is None:
    #     new_node.next = None
    #     temp.next = new_node
    # temp = temp.next

    # DELETION

    def deletenode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next
        temp = None

    # def printlist(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.data, end=" ")
    #         temp = temp.next


if __name__ == '__main__':
    arr = Linkedlist()
    arr.head = Node(1)
    second = Node(2)
    third = Node(3)
    arr.head.next = second
    second.next = third
    third.next = arr.head
    # arr.push(3)
    # arr.push(4)
    # arr.push(5)
    arr.insertafter(arr.head.next.next,7)

    arr.printList()
