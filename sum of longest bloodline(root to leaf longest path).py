#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
def sumChecker(root):
    if root is None:
        return [0,0]
    l = sumChecker(root.left)
    r = sumChecker(root.right)
    if l[0] == r[0]:
        if l[1] > r[1]:
            l[0] += 1
            if root:
                l[1] += root.data
            return l
        else:
            r[0] += 1
            if root.data:
                r[1] += root.data
            return r
    if l[0] > r[0]:
        l[0] += 1
        if root:
            l[1] += root.data 
        return l
    else:
        r[0] += 1
        if root:
            r[1] += root.data
        return r
        
def sumOfLongRootToLeafPath(root):
    if root is None:
        return 0
    T = sumChecker(root)
    return T[1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#CONTRIBUTED BY RavinderSinghPB
from collections import defaultdict
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        
        print(sumOfLongRootToLeafPath(tree.root))
# } Driver Code Ends
