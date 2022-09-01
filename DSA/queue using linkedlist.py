class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.f = -1
        self.b = 0

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def append(self, new_data):

        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        self.b += 1

    def deletion(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp = None
        self.f = (self.f+1)%self.b

    def front(self):
        return f"\nfront is at {self.f}"

    def end(self):
        return f"\nend is at {self.b} "

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    q = Linkedlist()
    q.head = Node(1)

    q.head.next = None
    q.append(5)
    q.append(3)
    q.append(6)
    q.append(4)
    q.printlist()
    print(q.end())
    q.deletion()
    q.printlist()
    print(q.front())
    print(q.end())