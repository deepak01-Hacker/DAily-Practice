# Your task is to complete this function
# function should return true/false or 1/0

def util(root,min,max):
    if root is None:
        return False
    if (root.data-1 == min and root.data+1 == max):
        return True
    return util(root.left,min,root.data) or util(root.right,root.data,max)
    

def isdeadEnd(root):
    return util(root,0,201)
