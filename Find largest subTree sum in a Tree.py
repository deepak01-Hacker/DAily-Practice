def sumUtil(root,resMax):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    l = sumUtil(root.left,resMax)
    r = sumUtil(root.right,resMax)
    temp = l+r+root.data
    if temp > resMax[0]:
        resMax[0] = temp
    return temp

def findLargestSum(root):
    if root is None:
        return 0
    resMax = [-10**6] 
    return sumUtil(root,resMax)
