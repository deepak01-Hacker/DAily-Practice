#User function Template for python3
def minimumPlatform(n,arr,dep):
    
    temp = [0]*2400
    
    for i in range(n):
        temp[int(arr[i])] += 1
        temp[int(dep[i])+1] -= 1
    
    min_ = 0
    for i in range(1,2400):
        temp[i] += temp[i-1]
        if temp[i] > min_:
            min_ = temp[i]
    return min_
        
    
