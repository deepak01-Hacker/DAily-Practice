#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


# Returns the LCA of the nodes with values n1 and n2
# in the BST rooted at 'root' 

def LCAs(root,n1,n2):
    if root is None:
        return Node(-1)
    if (root.data > n1 and root.data < n2) or (root.data == n1 and root.data < n2) or (root.data == n2 and root.data > n1):
        return root
    if (root.data > n1):
        return LCAs(root.left,n1,n2)
    elif (root.data < n1):
        return LCAs(root.right,n1,n2)
  
def LCA(root, n1, n2):
    return LCAs(root,min(n1,n2),max(n1,n2))
