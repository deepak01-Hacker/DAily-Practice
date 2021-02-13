#User function Template for python3

'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
'''
def nextLargerElement(arr,n):
    res = []
    stack = []
    i = n-1
    while(i>=0):
        if stack == []:
            res.append(-1)
            stack.append(arr[i])
            i -= 1
        elif stack[-1] > arr[i]:
            res.append(stack[-1])
            stack.append(arr[i])
            i -= 1
        else:
            stack.pop()
            
    return res[::-1]
            
