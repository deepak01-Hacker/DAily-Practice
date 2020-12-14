def isValid(arr,M,N,mid):
    allocat = 0
    sum = 0
    t = False
    for i in range(N):
        sum += arr[i]
        if sum>mid :
            allocat += 1
            sum = arr[i]
        if (N-i == M-allocat):
            allocat += 1
            sum = arr[i]
            t = True
    if sum and sum < mid and t != True:
        allocat += 1
    if allocat == M:
        return True
    return False


def findPages(arr,N,M):
    left = max(arr)
    right = sum(arr)
    res = right
    while(left<=right):
        mid = (left+right)//2
        if isValid(arr,M,N,mid):
            right = mid-1
            res = min(res,mid)
        else:
            left = mid+1

    return res
