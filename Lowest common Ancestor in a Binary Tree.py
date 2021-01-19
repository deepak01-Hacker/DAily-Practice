def dHelp(root,a,b,mins):
    if root is None:
        return False
    l = dHelp(root.left,a,b,mins)
    r = dHelp(root.right,a,b,mins)
    if l and r:
        mins[0] = root
    if (l and (b == root.data or a == root.data)) or (r and (b == root.data or a == root.data)):
        mins[0] = root
        return False
    if root.data == a:
        return True
    elif root.data == b:
        return True
    if l or r:
        return True
    return False
    
def lca(root, n1, n2):
    if root is None:
        return 0
    mins = [Node(10001)]
    dHelp(root,n1,n2,mins)
    return mins[0]
    
