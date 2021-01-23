def TreefromBST(st):
    root = Node(st[0])
    stack.append(root)
    for i in range(1,len(st)):
        tempHead = root
        while(tempHead):
            if tempHead.data < st[i]:
                if tempHead.right is None:
                    tempHead.right = Node(st[i])
                    break
                tempHead = tempHead.right
            elif tempHead.data > st[i]:
                if tempHead.left is None:
                    tempHead.left = Node(st[i])
                    break
                tempHead = tempHead.left
    return root
    
    
    ----------------------o(n) approach from geeksforgeeks --------------------------------
    
    
def getPreIndex():
    return constructTreeUtil.preIndex
 
 
def incrementPreIndex():
    constructTreeUtil.preIndex += 1
 
# A recursive function to construct BST from pre[].
# preIndex is used to keep track of index in pre[]
 
 
def constructTreeUtil(pre, key, mini, maxi, size):
 
    # Base Case
    if(getPreIndex() >= size):
        return None
 
    root = None
 
    # If current element of pre[] is in range, then
    # only it is part of current subtree
    if(key > mini and key < maxi):
 
        # Allocate memory for root of this subtree
        # and increment constructTreeUtil.preIndex
        root = Node(key)
        incrementPreIndex()
 
        if(getPreIndex() < size):
 
            # Construct the subtree under root
            # All nodes which are in range {min.. key} will
            # go in left subtree, and first such node will
            # be root of left subtree
            root.left = constructTreeUtil(pre,
                                          pre[getPreIndex()], 
                                          mini, key, size)
        if(getPreindex() < size):
 
            # All nodes which are in range{key..max} will
            # go to right subtree, and first such node will
            # be root of right subtree
            root.right = constructTreeUtil(pre,
                                           pre[getPreIndex()], 
                                           key, maxi, size)
 
    return root
