def mergeSorted(arr1,arr2,m,n):
    for i in range(n-1,-1,-1):

        last = arr1[m-1]
        j = m-2
        while(j>=0 and arr1[j] >arr2[i]):
            arr1[j+1] = arr1[j]
            j -= 1
        if (j != m-2 or last > arr2[i]):
            arr1[j+1] = arr2[i]
            arr2[i] = last
    return arr1+arr2
if __name__ == "__main__":
    arr1 = [10,12,14]  
    arr2 = [5,18,20]   
    print(mergeSorted(arr1,arr2,len(arr1),len(arr2)))
