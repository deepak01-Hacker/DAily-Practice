
def pathUtil(root,k,path):
    if root is None:
        return 
    path.append(root.data)
    pathUtil(root.left,k,path)
    pathUtil(root.right,k,path)
    t = 0
    for value in range(len(path)-1,-1,-1):
        t += path[value]
        if t == k:
            print(*path[value:])
    path.pop(-1)

def printAllpaths(root,k):
    if root is None:
        return 
    path = []
    pathUtil(root,k,path)
    return 
