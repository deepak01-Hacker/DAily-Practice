N = 5
  
# array for storing the  
# current index of list i 
ptr = [0 for i in range(501)] 
  
# This function takes an k sorted  
# lists in the form of 2D array as  
# an argument. It finds out smallest 
# range that includes elements from  
# each of the k lists. 
def findSmallestRange(arr, n, k): 
  
    i, minval, maxval, minrange, minel, maxel, flag, minind = 0, 0, 0, 0, 0, 0, 0, 0
          
    # initializing to 0 index 
    for i in range(k + 1): 
        ptr[i] = 0
  
    minrange = 10**9
          
    while(1):     
          
            # for mainting the index of list  
            # containing the minimum element 
        minind = -1
        minval = 10**9
        maxval = -10**9
        flag = 0
  
        # iterating over all the list 
        for i in range(k): 
              
                # if every element of list[i] is  
                # traversed then break the loop 
            if(ptr[i] == n): 
                flag = 1    
                break
  
            # find minimum value among all the list  
            # elements pointing by the ptr[] array  
            if(ptr[i] < n and arr[i][ptr[i]] < minval): 
                minind = i # update the index of the list 
                minval = arr[i][ptr[i]] 
              
            # find maximum value among all the  
            # list elements pointing by the ptr[] array 
            if(ptr[i] < n and arr[i][ptr[i]] > maxval): 
                maxval = arr[i][ptr[i]] 
              
          
  
        # if any list exhaust we will  
        # not get any better answer, 
        # so break the while loop 
        if(flag): 
            break
  
        ptr[minind] += 1
  
        # updating the minrange 
        if((maxval-minval) < minrange): 
            minel = minval 
            maxel = maxval 
            minrange = maxel - minel 
      
    print("The smallest range is [", minel, maxel, "]") 
  
# Driver code 
arr = [ 
    [4, 7, 9, 12, 15], 
    [0, 8, 10, 14, 20], 
    [6, 12, 16, 30, 50] 
    ] 
  
k = len(arr) 
  
findSmallestRange(arr, N, k) 
