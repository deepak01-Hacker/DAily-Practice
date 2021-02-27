def heapify(arr,n,curr):
    
    largest = curr
    left = 2*curr+1
    right = 2*curr+2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != curr:
        arr[curr],arr[largest] = arr[largest],arr[curr]
        heapify(arr,n,largest)
    


def mergeTwoBinaryMaxHeap(n1,n2,arr1,arr2):
    arr = arr1+arr2
    n = n1+n2
    startIndex = n//2-1
    for i in range(startIndex,-1,-1):
        heapify(arr,n,i)
    print(*arr)
    


if __name__ == "__main__":
    for _ in range(int(input())):
        n1,n2 = map(int,input().split(" "))
        arr1 = list(map(int,input().rstrip().split(" ")))
        arr2 = list(map(int,input().rstrip().split(" ")))
        mergeTwoBinaryMaxHeap(n1,n2,arr1,arr2)
