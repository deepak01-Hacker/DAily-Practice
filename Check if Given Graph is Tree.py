def isCycleUtil(v,visited,parent,graph):

    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            if isCycleUtil(i,visited,v,graph) == True:
                return True
        elif i != parent:
            return True
    return False

def isTree(graph,V):
    visited = [False] *V
    if isCycleUtil(0,visited,-1,graph) == True:
        return False
    for i in range(V):
        if visited[i] == False:
            return False
    return True

