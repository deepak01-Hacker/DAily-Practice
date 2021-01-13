
#Diameter of Binary Tree /////////////////////////


def diameters(root,ans):
    if root is None :
        return 0
    l = diameters(root.left,ans)
    r = diameters(root.right,ans)
    tl = l
    tr = r
    if l > r:
        tl = l+1
    else:
        tr = r+1
    ans[0] = max(ans[0],tl+tr)
    return tl if tl > l else tr
    

def diameter(root):
    ans = [0]
    diameters(root,ans)
    return ans[0]
