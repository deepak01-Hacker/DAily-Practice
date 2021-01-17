def checker(root,Hd,ans,t):
    if root is None:
        return 
    if root.left is None and root.right is None:
        if t[0] == -1:
            t[0] = Hd
        else:
            ans[0] = t[0] == Hd and ans[0] 
        return 
    checker(root.left,Hd+1,ans,t)
    checker(root.right,Hd+1,ans,t)

def check(node):
    ans = [True]
    t = [-1]   
    checker(root,0,ans,t)
    return ans[0]
