import sys

class Graph:
    
    def __init__(self,v):
        self.V = v
        self.graph = [[0 for _ in range(v)] for _ in range(v)]

    def mins(self,key,mstSet):

        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                minindex = v
        return minindex 

    def prints(self,parent):
        
        for v in range(1,self.V):
            print(parent[v],v,self.graph[parent[v]][v])

    def prims(self):
        key = [sys.maxsize]*self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent = [None] * self.V
        parent[0] = -1

        for cut in range(self.V):
            
            u = self.mins(key,mstSet)

            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and key[v] > self.graph[u][v] and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        
        self.prints(parent) 

if __name__ == "__main__":
    G = Graph(4)
    G.graph = [[0,10,6,5],
               [10,0,15,0],
               [6,0,4,0],
               [5,15,4,0]]
    G.prims()
