#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if l > r:
            return l+1
        else:
            return r+1

