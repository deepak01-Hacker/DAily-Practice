

#User function Template for python3

# Return the size of the largest sub-tree which is also a BST
min_val = -2**31
max_val = 2**31

def util(root,ans):
    if root is None:
        return [True,min_val,max_val,0]
    l = util(root.left,ans)
    r = util(root.right,ans)
    if l[0] and r[0] and (root.data > l[1] and root.data < r[2]):
        p = [True,max(root.data,r[1]),min(root.data,l[2]),l[3]+r[3]+1]
        ans[0] = max(ans[0],(l[3]+r[3]+1))
    else:
        p = [False,min_val,max_val,0]
    return p
    

def largestBst(root):
    ans = [0]
    util(root,ans)
    return ans[0]
