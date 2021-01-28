def flattenBSTtoSortedListutil(root,arr):
    if root is None:
        return 
    flattenBSTtoSortedListutil(root.left,arr)
    arr.append(root.data)
    flattenBSTtoSortedListutil(root.right,arr)
    
    
def flattenBSTtoSortedList(root):
  arr = []
  flattenBSTtoSortedListutil(root,arr)
  return arr
