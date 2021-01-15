#User function Template for python3


'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


 # This function should return tree if passed  tree 
 # is balanced, else false.  Time complexity should
 # be O(n) where n is number of nodes in tree */
 
def check(root,mp):
    if root is None:
        return 0
    l = check(root.left,mp)
    r = check(root.right,mp)
    Lr = l
    Rr = r
    if l > r:
        Lr += 1
    else:
        Rr += 1
    mp[0] = max(mp[0],abs(Lr-Rr))
    return Lr if Lr > l else Rr
    
def isBalanced(root):
    if root is None:
        return True 
    mp = [0]
    check(root,mp)
    return False if mp[0] > 2 else True
