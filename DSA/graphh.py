class graph():
    # construsting a list
    def __init__(self):
        self.list = {}

    # creating graph with the help of dictionary
    def createEdge(self, start, end):
        if start in self.list.keys():
            self.list[start].append(end)
        else:
            self.list[start] = [end]

    # Displaying all the nodes
    def display(self):
        for i in self.list:
            print(i, '-->', ' --> '.join([str(j) for j in self.list[i]]))

    # traversing with BFS

    def BFS(self, startNode):
        visited = [False] * len(self.list)
        queue = []

        visited[startNode] = True
        queue.append(startNode)

        while queue:
            startNode = queue.pop(0)
            print(startNode, end=" ")

            for i in self.list:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self,start):
        stack = [start]
        path = []

        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for i in self.list[vertex]:
                stack.append(i)

        return path




g = graph()
g.createEdge(0, 1)
g.createEdge(0, 4)
g.createEdge(1, 4)
g.createEdge(1, 5)
g.createEdge(5, 3)
g.createEdge(1, 2)
g.createEdge(2, 3)
g.createEdge(2, 5)
g.createEdge(3, 4)
g.createEdge(3, 5)
g.createEdge(4, 6)
g.createEdge(6, 0)

g.display()
print(g.DFS(5))
