
#CODE COPIED FROM GFG


INT_MIN = -2**31
INT_MAX = 2**31
 
# Function to find postorder traversal
# from preorder traversal.
 
 
def findPostOrderUtil(pre, n, minval,
                      maxval, preIndex):
 
    # If entire preorder array is traversed
    # then return as no more element is left
    # to be added to post order array.
    if (preIndex[0] == n):
        return
 
    # If array element does not lie in
    # range specified, then it is not
    # part of current subtree.
    if (pre[preIndex[0]] < minval or
            pre[preIndex[0]] > maxval):
        return
 
    # Store current value, to be printed later,
    # after printing left and right subtrees.
    # Increment preIndex to find left and right
    # subtrees, and pass this updated value to
    # recursive calls.
    val = pre[preIndex[0]]
    preIndex[0] += 1
 
    # All elements with value between minval
    # and val lie in left subtree.
    findPostOrderUtil(pre, n, minval,
                      val, preIndex)
 
    findPostOrderUtil(pre, n, val,
                      maxval, preIndex)
                      
    print(val, end=" ")
 


def constructTree(pre, size):
    preIndex = [0]
    findPostOrderUtil(pre, len(pre), INT_MIN,INT_MAX, preIndex)

