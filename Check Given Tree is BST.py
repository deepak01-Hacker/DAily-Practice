#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def check(root,min,max):
    if root is None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return check(root.left,min,root.data) and check(root.right,root.data,max)
    
def isBST(root):
    IntMax = 2147483647
    IntMin = -2147483648
    return check(root,IntMin,IntMax)
