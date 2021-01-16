#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

def search(tDAta,ino,start,end):
    for i in range(start,end+1):
        if ino[i] == tDAta:
            return i
def constructTree(ino,pre,start,end):
    if end < start:
        return None
    root = Node(pre[0])
    pre.pop(0)
    if start == end:
        return root
    index = search(root.data,ino,start,end)
    root.left = constructTree(ino,pre,start,index-1)
    root.right = constructTree(ino,pre,index+1,end)
    return root
    
def buildtree(ino, pre, n):
    return constructTree(ino,pre,0,n-1)

