#Python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
    Code and Logic From GeeksForGeeks
"""
#Tags : Medium , Array , GeeksForGeeks , Nearly Sorted Array

#complexity : O(NlogN)
#Auxiliray Space : O(n**2)

def mergeSort(arr,n):
    temp_arr = [0]*n
    mergesort(arr,temp_arr,0,n-1)

def mergesort(arr,temp_arr,left,right):
    inversion_count = 0
    if left < right:

        mid = (left+right)//2

        inversion_count += mergesort(arr,temp_arr,left,mid)
        inversion_count += mergesort(arr,temp_arr,mid+1,right)
        inversion_count += merge(arr,temp_arr,left,mid,right)
    return inversion_count 

def merge(arr,temp_arr,left,mid,right):
    i = left
    j = mid+1
    k = left
    inver = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            inver += mid-i+1
            temp_arr[k] = arr[j]
            j += 1
            k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for val in range(left,right+1):
        arr[val] = temp_arr[val]
    return inver

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        mergeSort(arr,n)
        



#/////////////////////////////////////////////////////////////////////////////////////////////////
#This Code is Taken from gfg ;) bcz this is save my time to code this whole Problem,
def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 
  
arr = [1, 20, 6, 4, 5] 
n = len(arr) 
print("Number of inversions are", 
              getInvCount(arr, n)) 

#Happy Coding