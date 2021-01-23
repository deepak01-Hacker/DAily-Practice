# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minVal(self,root):
        temp = root
        while(temp.left):
            temp = temp.left
        return temp
    
    def deleteNode(self, root, k):
        if root is None:
            return None
        if (root.val > k):
            root.left = self.deleteNode(root.left,k)
        elif(root.val < k):
            root.right = self.deleteNode(root.right,k)
        else:
            
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.minVal(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right,temp.val)
            
        return root
        
