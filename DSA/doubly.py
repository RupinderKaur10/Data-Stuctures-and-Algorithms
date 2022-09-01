class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node

    def insertafter(self, prev_node, new_data):
        if prev_node is None:
            return f"please enter the node present in the list"
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

