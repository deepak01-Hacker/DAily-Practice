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

def merge(nodes1,nodes2):
    arr = []
    i = 0
    j = 0
    while (i < len(nodes1) and j < len(nodes2)):
        if nodes1[i] <= nodes2[j]:
            arr.append(nodes1[i])
            i += 1
        else:
            arr.append(nodes2[j])
            j += 1
    while(i<len(nodes1)):
        arr.append(nodes1[i])
        i += 1
    while(j<len(nodes2)):
        arr.apppend(nodes2[j])
        j += 1
    return arr

def mergeTwoBST(root1,root2):
    nodes1 = []
    storeBSTnodes(root1,nodes1)
    nodes2 = []
    storeBSTnodes(root2,nodes2)
    nodes = merge(nodes1,nodes2)
    return createTree(nodes)

