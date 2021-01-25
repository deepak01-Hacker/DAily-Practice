#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def searchUtil(root,ar):
    if root is None:
        return 
    searchUtil(root.left,ar)
    ar.append(root.data)
    searchUtil(root.right,ar)
    
def searchUtil2(root,ar):
    if root is None:
        return 
    searchUtil2(root.left,ar)
    root.data = ar[0]
    ar.pop(0)
    searchUtil2(root.right,ar)
    
def binaryTreeToBST(root):
    if root is None:
        return 
    ar = []
    searchUtil(root,ar)
    ar.sort()
    searchUtil2(root,ar)
    
    
