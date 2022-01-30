class Graph:
    def __init__(self,vertices):
 
        self.V = vertices
        self.graph = {}
        for i in range(self.V):
            self.graph[i] = []
 
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
        print(self.graph)

    def topoSort(self,node,visited,stack):
        visited[node] = True
        for child,weight in self.graph[node]:
            if visited[child]==False:
                self.topoSort(child,visited,stack)
        stack.append(node)

    def shortestPath(self,source):
        visited = [False]*self.V 
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topoSort(i,visited,stack)

        dist = [float('inf')]*self.V 
        dist[s] = 0

        while stack:
            node = stack.pop()
            if dist[node]!=float("inf"):
                for child, weight in self.graph[node]:
                    dist[child] = min(dist[child],dist[node]+weight)

        for i in range(self.V):
            print ("%d" %dist[i]) if dist[i] != float("Inf") else  print("Inf") ,

g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
 
# source = 1
s = 3
 
print ("Following are shortest distances from source %d " % s)
g.shortestPath(s)
