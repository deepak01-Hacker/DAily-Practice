def createTree(st):
    stackRoot = []
    for i in range(len(st)):
        if st[i] == "(":
            continue
        elif st[i] == ")":
            temp = stackRoot.pop()
            #print(temp.data,stackRoot[-1].data)
            if len(stackRoot) >= 1:
                if stackRoot[-1].left is None:
                    stackRoot[-1].left = temp
                elif stackRoot[-1].right is None:
                    stackRoot[-1].right = temp
            elif len(stackRoot) == 0:
                root = stackRoot[0]
        else:
            stackRoot.append(Node(st[i]))
    return stackRoot[0]
