def findElement(arr, ranges, rotations, index) : 
      
    for i in range(rotations - 1, -1, -1 ) : 
      
        
        left = ranges[i][0] 
        right = ranges[i][1] 
  
        
        print(left,index,right)
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1
        print(left,index,right,2)
        
        
    return arr[index] 
  

arr = [ 1, 2, 3, 4, 5 ] 


rotations = 2
  

ranges = [ [ 0, 2 ], [ 0, 3 ]] 
  
index = 0
  
print(findElement(arr, ranges, rotations, index)) 