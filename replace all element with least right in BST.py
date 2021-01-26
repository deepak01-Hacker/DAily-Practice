
def replaceRight(root):
    if root is None:
        return -1
    if root.left is None and root.right is None:
        return root.data
    replaceRight(root.left)
    l = replaceRight(root.right)
    if l is None:
        root.data = -1
    else:
        root.data = l
