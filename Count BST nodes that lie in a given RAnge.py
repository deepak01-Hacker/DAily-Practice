#User function Template for python3

##Structure of node
'''
# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
'''
##Complete this function
def inor(root,low,high,c):
    if root is None:
        return 
    if root.data >= low and root.data <= high:
        c[0] += 1
    inor(root.left,low,high,c)
    inor(root.right,low,high,c)

def getCount(root,low,high):
    c = [0]
    inor(root,low,high,c)
    return c[0]
