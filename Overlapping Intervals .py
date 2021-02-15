def overlapped(parr,n):
    stack = []
    parr.sort(key = lambda x : x[1])
    stack.append(parr[0])

    for i in range(1,n):
        if stack[-1][1] <= parr[i][0]:
            stack.append(parr[i])
        else: 
            stack[-1][1] = parr[i][1]

    return stack
