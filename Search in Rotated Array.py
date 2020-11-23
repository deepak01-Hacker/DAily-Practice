def binarySearch(arr,tr):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = (start + end)//2
        if arr[mid] == tr:
            return mid
        elif ((tr <= arr[end] and arr[mid] > arr[end]) or( tr > arr[mid])):
            start = mid+1
        else:
            end = mid-1
    return -1
        
        

if __name__ == "__main__":
    arr = list(map(int,input().rstrip().split(" ")))
    tr = int(input())
    print(binarySearch(arr,tr))
