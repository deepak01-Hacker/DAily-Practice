def findPivot(arr,lowerBound,upperbound):
    low = lowerBound
    high = upperbound
    while(low<=high):
        mid = low+(high)//2
        print(low,high,mid)
        if mid == lowerBound:
            if mid == upperbound:
                return mid
            elif arr[mid] >= arr[mid+1]:
                return mid
        elif mid == upperbound:
            if arr[mid] >= arr[mid-1]:
                return mid
        else:
            if arr[mid] >= arr[mid+1] and arr[mid] >= arr[mid-1]:
                return mid
            elif arr[mid] > arr[high]:
                low = mid+1
            elif arr[mid] < arr[high]:
                high = mid
            else:
                return -1
        

if __name__ == "__main__":
    arr = [4,5,6,1,2,3]
    print(findPivot(arr,0,len(arr)-1))
    
