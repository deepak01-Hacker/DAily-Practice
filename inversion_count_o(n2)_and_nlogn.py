#MErge sOrt 
#Count Inversion

#o(n^2)
def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 


# -------------------------------------------------------------------------#-----------------------------------------------------



def mergeSort(arr,n):
    
    temp_arr = [0]*n
    return _mergeSort(arr,temp_arr,0,n-1)

def _mergeSort(arr,temp_arr,left,right):
    
    inv_count = 0
    
    if left < right:

        mid = (left+right)//2

        inv_count += _mergeSort(arr,temp_arr,left,mid)

        inv_count += _mergeSort(arr,temp_arr,mid+1,right)

        inv_count += merge(arr,temp_arr,left,mid,right)
    return inv_count

def merge(arr,temp_arr,left,mid,right):

    i = left
    j = mid+1
    k = left
    inv_count = 0

    while i <= mid  and j <= right:

        if arr[i]<=arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i+1)
            k += 1
            j += 1
    while(i<=mid):
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while(j<=right):
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop in range(left,right+1):
        arr[loop] = temp_arr[loop]
    return inv_count

if __name__ == "__main__":
    arr = [1,20,6,4,5]
    n = len(arr)
    print(mergeSort(arr,n))
