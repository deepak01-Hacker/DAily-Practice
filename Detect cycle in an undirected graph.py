class Solution:
    def utilCycle(self,v,adj,visited,parent):
        visited[v] = True
        
        for vt in adj[v]:
            if visited[vt] == False :
                if self.utilCycle(vt,adj,visited,v):
                    return True
            elif parent != vt:
                return True
                
        return False

    
	def isCycle(self, V, adj):
	    visited = [False]*V
	    for v in range(V):
	        if visited[v] == False:
	            if self.utilCycle(v,adj,visited,-1):
	                return True
	    return False
