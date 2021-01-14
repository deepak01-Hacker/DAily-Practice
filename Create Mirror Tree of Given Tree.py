def mirrorTree(root,mirror):
    if root is None:
        mirror = None
        return mirror
    mirror = Node(root.data)
    mirror.right = mirrorTree(root.left,mirror.left)
    mirror.left  = mirrorTree(root.right,mirror.right)
    return mirror
