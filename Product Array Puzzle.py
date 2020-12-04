#User function Template for python3

def productS(arr,start,end):
    t = 1
    zero = 0
    for i in range(start,end):
        t *= arr[i]
        if arr[i] == 0:
            zero += 1
    if arr[0] == 0:
        zero += 1
    
    return [t,zero]
    
def Except(arr,po,n):
    t = 1
    for i in range(n):
        if po != i:
            t *= arr[i]
    return t

def productExceptSelf(arr,n):
    ans = []
    pro = productS(arr,1,n)
    prod = pro[0]
    ans.append(prod)
    for i in range(1,n):
        if prod == arr[i] and arr[i] == 0 and pro[1] < 2:
            prod = Except(arr,i,n)
            prod = prod//arr[i-1]
        elif arr[i] == 0:
            prod = 0
        else:
            prod = prod//arr[i]
        prod *= arr[i-1]
        ans.append(prod)
    return ans
        
