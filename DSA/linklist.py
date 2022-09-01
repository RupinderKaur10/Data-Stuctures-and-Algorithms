class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        x

class Linkedlist:
    def __init__(self):
        self.head = None

    # INSERTION
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertafter(self, prev_node, new_data):

        if prev_node is None:
            return f"please enter the node present in the list"
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        # if temp.next is None:
        #     new_node.next = None
        #     temp.next = new_node
        # temp = temp.next

    # DELETION

    def deletenode(self, key):
        temp = self.head
        #deleting from front
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # deleting from end
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if list is empty
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = Linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    third.next = None
    # llist.printlist()
    llist.push(4)
    # llist.printlist()
    llist.insertafter(llist.head.next, 5)
    llist.append(6)
    # llist.printlist()
    # llist.deletenode()
    llist.printlist()
