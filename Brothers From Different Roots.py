#User function Template for python3

# Class structure used:- 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None

def inor(root,BST_set):
    if root is None:
        return 
    BST_set.add(root.data)
    inor(root.left,BST_set)
    inor(root.right,BST_set)

def checker(root,BST_set,x,ans):
    if root is None:
        return 
    if (x-root.data) in BST_set:
        ans[0] += 1
    checker(root.left,BST_set,x,ans)
    checker(root.right,BST_set,x,ans)
    

def countPairs(root1, root2, x):
    BST_set = set()
    inor(root1,BST_set)
    ans = [0]
    checker(root2,BST_set,x,ans)
    return ans[0]
