
#Use mind not hand ; __ )


def mergeSort(arr,left,right):
    if left<right:
        mid = (left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        sort(arr,left,right,mid)
    return 
def sort(arr,left,right,mid):
    i = left
    j = mid+1
    while(i<= mid and j <= right):
        if arr[i] <= arr[j]:
            i += 1
        else:
            value = arr[j]
            index = j
            while(i!= index):
                arr[index] = arr[index-1]
                index -= 1
            arr[i] = value
            mid += 1
            j += 1
            i += 1




if __name__ == "__main__":
    arr = [1,20,6,4,5]
    n = len(arr)
    mergeSort(arr,0,n-1)
    print(arr)
