v = 4
class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = [[] for i in range(v)]
    def addEdge(self,u,v):
        self.graph[v].append(u)
        self.graph[u].append(v)

    def printgraph(self):
        for i in range(self.v):
            print(i,end="-")
            for j in range(len(self.graph[i])):
                print(self.graph[i][j],end=" ")
            print()

g = Graph(4)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(0,2)
g.addEdge(1,2)
g.printgraph()