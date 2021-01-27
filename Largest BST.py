def util(root,ans):
    if root is None:
        return [0,True]
    if root.left is None and root.right is None:
        ans[0] = max(ans[0],1)
        return [1,True]
    l = util(root.left,ans)
    r = util(root.right,ans)
    if l[1] and r[1]:
        left = -1 if root.left is None else root.left.data
        right = 1000000 if root.right is None else root.right.data
        if left < root.data and right > root.data:
            temp = max(l[0],r[0])+1
            ans[0] = max(ans[0],temp)
            return [temp,True]
    return [0,False]


def largestBst(root):
    ans = [0]
    util(root,ans)
    return ans[0]
