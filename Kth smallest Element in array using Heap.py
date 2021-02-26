import heapq

def kLargest(arr, n, k):
	
	heap = []
	
	if k > n:
		return heap
		
	heapq.heapify(heap)
	
	for i in range(n):
		
		heapq.heappush(heap,-arr[i])
		
		if len(heap) > k:
			heapq.heappop(heap)

	print(heapq.heappop(heap)*-1)

