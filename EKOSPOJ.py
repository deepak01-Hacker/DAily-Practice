#Problem Link :https://www.spoj.com/problems/EKO/


def isValid(arr,M,N,mid):
    allocat = 0
    for i in range(N):
        if arr[i] >= mid:
            allocat += arr[i]-mid
    if allocat >= M:
        return True
    return False



def allocatpages(arr,M,N):
    left = min(arr)
    right = max(arr)
    res = -1
    while(left<=right):
        mid = (left+right)//2
        if isValid(arr,M,N,mid):
            left = mid+1
            res = max(res,mid)
        else:
            right = mid-1
    return res



if __name__ == "__main__":
    N,M = map(int,input().split(" "))
    arr = list(map(int,input().rstrip().split(" ")))
    print(allocatpages(arr,M,N))
