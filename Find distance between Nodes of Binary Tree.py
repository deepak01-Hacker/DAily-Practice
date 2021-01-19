def dHelp(root,a,b,mins):
    if root is None:
        return [0,0]
    l = dHelp(root.left,a,b,mins)
    r = dHelp(root.right,a,b,mins)
    if l[1] and b == root.data:
        mins[0] = l[1]
        return [0,0]
    elif r[1] and a == root.data:
        mins[0] = r[1]
        return [0,0]
    if l[1] > 0 and r[1] > 0 :
        mins[0] = l[1] +r[1]
    if l[1]:
        return [a,l[1]+1]
    if r[1]:
        return [b,r[1]+1]
    if a == root.data:
        return [a,1]
    if b == root.data:
        return [b,1]
    return [0,0]
    
    
def findDist(root,a,b):
    mins = [0]
    dHelp(root,a,b,mins)
    return mins[0]
