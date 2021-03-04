class Graph():

    def __init__(self,V):
        self.adjlist = [[] for _ in range(V)]
        self.V = V
    
    def addEdge(self,u,v):
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)

    def bfs(self):
        visited = [False for _ in range(self.V)]
        queue = []
        queue.append(0)
        while(queue):
            front = queue.pop(0)
            if visited[front] != True:
                print(front,end=" ")
                visited[front] = True
            for Edge in self.adjlist[front]:
                if visited[Edge]!=True:
                    queue.append(Edge)
        print()

    def dfs_util(self,visited,src):
        visited[src] = True
        print(src,end=" ")
        for v in self.adjlist[src]:
            if visited[v] != True:
                self.dfs_util(visited,v)

    def dfs(self):
        visited = [False for _ in range(self.V)] 
        self.dfs_util(visited,0)


if __name__ == "__main__":
    G1 = Graph(5)
    G1.addEdge(0,1)
    G1.addEdge(0,2)
    G1.addEdge(1,2)
    G1.addEdge(2,4)
    G1.addEdge(3,1)
    G1.addEdge(4,1)
    G1.dfs()
