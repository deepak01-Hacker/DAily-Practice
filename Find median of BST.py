def counter(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return (counter(root.left)+counter(root.right))+1

def sortedBST(root,median):
    if root is None:
        return
    sortedBST(root.left,median)
    if median[1] == 1:
        median[0] = root.data
    median[1] = median[1]- 1
    sortedBST(root.right,median)

def findMedian(root):
    countNodes = counter(root)
    median = [-1,(countNodes//2)+ (0 if countNodes %2 == 0 else 1)]
    sortedBST(root,median)
    return median[0]
