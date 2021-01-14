def bottomView(root):
    if root is None:
        return []
    result = []
    map = {}
    stack = []
    stack.append([root,0])
    while(stack):
        tempPop = stack.pop(0)
        curr = tempPop[0]
        Hd = tempPop[1]
        map[Hd] = curr.data
        if curr.left:
            stack.append([curr.left,Hd-1])
        if curr.right:
            stack.append([curr.right,Hd+1])
    for value in sorted(map):
        result.append(map[value])
    return result



