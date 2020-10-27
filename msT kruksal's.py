class Graph:
    
    def __init__(self,V):
        self.V = V
        self.graph = []
    
    def addedge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    
    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)

        if rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        elif rank[yroot] > rank[xroot]:
            parent[xroot] = yroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1 
    
    def kruksal(self):
        
        self.graph = sorted(self.graph,key = lambda item:item[2])
        
        result = []
        parent = []
        rank = []
        for i in range(0,self.V):
            parent.append(i)
            rank.append(0)
        i_graph = 0
        i_result = 0
        while(i_result < self.V-1):
            u,v,w = self.graph[i_graph]
            i_graph += 1
            x = self.find(parent,u)
            y = self.find(parent,v)

            if x != y:
                i_result+=1
                result.append([u,v,w])
                self.union(parent,rank,u,v)
        return result



if __name__ == "__main__":
    G = Graph(4)
    G.addedge(0,1,10)
    G.addedge(0,2,6)
    G.addedge(0,3,5)
    G.addedge(1,3,15)
    G.addedge(2,3,4)
    print(G.kruksal())
