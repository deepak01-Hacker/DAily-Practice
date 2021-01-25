def storeBSTnodes(root,nodes):
    if root is None:
        return
    storeBSTnodes(root.left,nodes)
    nodes.append(root.data)
    storeBSTnodes(root.right,nodes)

def createTree(nodes,start,end):
    if end>start:
        return
    mid = (start+end)//2
    root = Node(nodes[mid])
    root.left = createTree(nodes,start,mid-1)
    root.right = createTree(nodes,mid+1,end)
    return root
    

def balanceBST(root):
    nodes = []
    storeBSTnodes(root,nodes)
    return createTree(nodes,0,len(nodes)-1)

