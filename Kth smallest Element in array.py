#User function Template for python3
import heapq

class Solution:

	def kLargest(self,arr, n, k):
	    
	    heap = []
	    
	    if k > n:
	        return heap
	        
	    heapq.heapify(heap)
	    
	    for i in range(n):
	        
	        heapq.heappush(heap,arr[i])
	        
	        if len(heap) > k:
	            heapq.heappop(heap)
	    
	    ans = []
	    for i in range(k):
	        k = heapq.heappop(heap)
	        ans.append(k)
	    return ans[::-1]
