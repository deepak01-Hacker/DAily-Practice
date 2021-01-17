
def isTree(root,t):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    temp = root.data
    res = isTree(root.left,t) + isTree(root.right,t)
    t[0] = temp == res and t[0]
    return res

def isSumTree(root):
    t = [True]
    isTree(root,t)
    return t[0]
