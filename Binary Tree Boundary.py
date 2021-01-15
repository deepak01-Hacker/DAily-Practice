#User function Template for python3


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return a list containing the boundary view of the binary tree
def leftView(root):
    if root is None:
        return 
    if root.left:
        print(root.data,end=" ")
        leftView(root.left)
    elif root.right:
        print(root.data,end=" ")
        leftView(root.right)

def rightView(root):
    if root is None:
        return 
    if root.right:
        rightView(root.right)
        print(root.data,end=" ")
    elif root.left:
        rightView(root.left)
        print(root.data,end=" ")
def bottomView(root):
    if root is None:
        return
    bottomView(root.left)
    if root.left is None and root.right is None:
        print(root.data,end=" ")
    bottomView(root.right)
#{ 
    
def printBoundaryView(root):
    print(root.data,end=" ")
    leftView(root.left)
    bottomView(root.left)
    bottomView(root.right)
    rightView(root.right)
    return []
