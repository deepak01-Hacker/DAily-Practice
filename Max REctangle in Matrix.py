def Nright(arr,n):
    stack = []
    res = [0]*n
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            res[i] = n
        while (len(stack) > 0 and stack[-1][0] >= arr[i]):
            stack.pop()
        if len(stack) == 0:
            res[i] = n
        else:
            res[i] = stack[-1][1]
        stack.append((arr[i],i))
    return res

def NearestSmall(arr,n):
    stack = []
    res = [0]*n
    for i in range(n):
        if len(stack) == 0:
            res[i] = -1
        while(len(stack) > 0 and stack[-1][0] >= arr[i]):
            stack.pop()
        if len(stack) == 0:
            res[i] = -1
        else:
            res[i] = stack[-1][1]
        stack.append((arr[i],i))
    return res

def hax(arr,n):
    left = NearestSmall(arr,n)
    right = Nright(arr,n)
    print(left,right,arr)
    maxs = -10**6
    for i in range(n):
        temp = arr[i] * (right[i]-left[i]-1)
        maxs = max(maxs,temp)
    print()
    return maxs


def maxRectangle(M,n,m):
    largest = 0
    for i in range(n):
        for j in range(m):
            if M[i][j] > 0  and i-1>= 0:
                M[i][j] += M[i-1][j]
            elif M[i][j] == 0:
                M[i][j] = 0
        largest = max(largest,hax(M[i],m))

    return largest

if __name__ == "__main__":
    M = [[0,0,1,1,0,0,0,0],
         [1,1,1,1,1,1,1,0]]
    print(maxRectangle(M,2,8))
