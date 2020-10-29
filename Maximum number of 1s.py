#User function Template for python3
class Solution:
    
    def first(self, arr, low, high): 
        if high >= low: 
              
            # Get the middle index  
            mid = low + (high - low)//2
      
            # Check if the element at  
            # middle index is first 1 
            if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1: 
                return mid 
      
            # If the element is 0,  
            # recur for right side 
            elif arr[mid] == 0: 
                return self.first(arr, (mid + 1), high) 
          
            # If element is not first 1,  
            # recur for left side 
            else: 
                return self.first(arr, low, (mid - 1)) 
        return -1
                
	def rowWithMax1s(self,arr, n, c):
	    maxs = 0
	    mins = -1
	    for i in range(n):
	        index = self.first(arr[i],0,c-1)
	        if index != -1 and c-index > maxs:
	            maxs = c-index
	            mins = i
	    return mins
	        
