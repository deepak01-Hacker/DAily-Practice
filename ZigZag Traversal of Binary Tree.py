#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# return a list containing the zig zag level order traversal of the given tree
def zigZagTraversal(root):
    if root is None:
        return []
    result = []
    stack = []
    level = 0
    stack.append(root)
    while(True):
        len_ = len(stack)
        if len_:
            In = len(result)
            while(len_):
                curr = stack.pop(0)
                if level%2!=0:
                    result.insert(In,curr.data)
                else:
                    result.append(curr.data)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                len_ -= 1
            level += 1
                
        else:
            break
    return result
