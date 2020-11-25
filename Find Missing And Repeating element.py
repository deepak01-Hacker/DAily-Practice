#O(n) and o(1) space

class Solution:
    def findTwoElement( self,arr, n): 
        R = -1
        M = -1
        for i in range(n):
            if arr[i] < 0:
                t = -arr[i]
            else:
                t = arr[i]
            if t<=n:
                if arr[t-1] < 0:
                    R = t
                else:
                    arr[t-1] = -arr[t-1]
    
    
        for i in range(n):
            if arr[i] > 0 and i+1 != R:
                M = i+1
                break
        return [R,M]
