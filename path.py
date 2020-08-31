#python3
"""
    Code from : GeeksforGeeks
    contact us:a9649060356@gmail.com
"""
#many questions explanation was wrong so you read question carefully


def maxPathSum(ar1,ar2 , m , n): 
      
    # initialize indexes for ar1[] and ar2[] 
    i, j = 0, 0
      
    # Initialize result and current sum through ar1[] and ar2[] 
    result, sum1, sum2= 0, 0, 0
      
    # Below 3 loops are similar to merge in merge sort 
    while (i < m and j < n): 
        
        # Add elements of ar1[] to sum1 
        if ar1[i] < ar2[j]: 
            sum1 += ar1[i] 
            i+=1
          
        # Add elements of ar2[] to sum1     
        elif ar1[i] > ar2[j]: 
            sum2 += ar2[j] 
            j+=1
          
        else:   # we reached a common point 
          
            # Take the maximum of two sums and add to result 
            result+= max(sum1,sum2)
            print(1,1,max(sum1,sum2),result) 
            # Update sum1 and sum2 for elements after this intersection point 
            sum1, sum2 = 0, 0
              
            # Keep updating result while there are more common elements 
            while (i < m and j < n and ar1[i]==ar2[j]): 
                result += ar1[i] 
                i+=1
                j+=1
    # Add remaining elements of ar1[] 
    while i < m: 
        sum1 += ar1[i] 
        i+=1
    # Add remaining elements of b[] 
    while j < n: 
        sum2 += ar2[j] 
        j+=1
      
    print(2,max(sum1,sum2))
    result += max(sum1,sum2) 
      
    return result


for _ in range(1):
    arr = [11, 12, 13, 15, 19, 22, 23, 24, 24, 25, 31, 33, 38, 39, 49, 49, 51, 51, 52, 60, 60, 61, 63, 64, 65, 66, 67, 67, 68, 69, 71, 72, 76, 80, 80, 83, 87, 90, 94, 96, 97, 99]
    arr2 = [0, 2, 3, 5, 7, 8, 8, 11, 12, 13, 17, 18, 18, 19, 20, 21, 22, 23, 24, 24, 25, 29, 32, 32, 33, 33, 33, 34, 35, 35, 37, 39, 39, 39, 45, 46, 47, 48, 49, 49, 51, 52, 52, 54, 57, 57, 58, 58, 59, 59, 60, 61, 62, 63, 65, 65, 70, 71, 71, 71, 71, 71, 72, 72, 74, 74, 75, 77, 78, 80, 83, 83, 84, 84, 86, 86, 92, 92, 94, 94, 94, 95, 95, 99, 99, 99]
    print(maxPathSum(arr,arr2,len(arr),len(arr2)))


    #Second code is wrong if you want understand that then implement with yourself
    common = list(set(arr) & set(arr2)) 
    common.sort()
    hash_arr1 = [0]*101
    hash_arr2 = [0]*101
    for i in range(len(arr)):
        hash_arr1[arr[i]] = i
    for j in range(len(arr2)):
        hash_arr2[arr2[j]] = j
    sums = 0
    for k in range(len(common)):
        if k == 0:
            sums += max(sum(arr[:hash_arr1[common[k]]+1]),sum(arr2[:hash_arr2[common[k]]+1]))
            print(sums)
        else:
            prev = common[k-1]
            curr = common[k]
            sums += max(sum(arr[hash_arr1[prev]+1:hash_arr1[curr]+1]),sum(arr2[hash_arr2[prev]+1:hash_arr2[curr]+1]))
            print(1,max(sum(arr[hash_arr1[prev]+1:hash_arr1[curr]+1]),sum(arr2[hash_arr2[prev]+1:hash_arr2[curr]+1])))
            print(sums)
    sums += max(sum(arr[hash_arr1[common[-1]]+1:]),sum(arr2[hash_arr2[common[-1]]+1:]))    
    print(sums,sum(arr2))    



    