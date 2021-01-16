def inorders(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        temp = root.data
        root.data = 0
        return temp
    temp = root.data
    lt = inorders(root.left)
    lr = inorders(root.right) 
    root.data = lt + lr
    return temp + root.data
