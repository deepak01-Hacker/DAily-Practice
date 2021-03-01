
def heapify(heap,i,n):
	left = 2*i+1
	right = 2*i+2
	smallest = i
	if left < n and heap[left][0] < heap[smallest][0]: 
		smallest = left
	if right < n and heap[right][0] < heap[smallest][0]:
		smallest = right
	if smallest != i:
		heap[smallest],heap[i] = heap[i],heap[smallest]
		heapify(heap,smallest,n)

def replaceElement(heap,x):
	n = len(heap)
	heap[0] = x
	heapify(heap,0,n)

def MAkeHeap(heap):
	n = len(heap)
	startIndex = len(heap)//2-1
	for i in range(startIndex,-1,-1):
		heapify(heap,i,n)

def smallestRange(arr):
	heap = []
	k = len(arr)
	max_ = 0
	for i in range(k):
		heapNOde = []
		heapNOde.append(arr[i][0])
		heapNOde.append(i)
		heapNOde.append(1)
		heap.append(heapNOde)
		max_ = max(arr[i][0],max_)
	MAkeHeap(heap)
	result = [-1,-1,10**9]
	while(True):
		root = heap[0]
		min_ = root[0]

		if result[2] > max_-min_+1:
			result[2] = max_-min_+1
			result[0] = min_
			result[1] = max_
		
		if root[2] < len(arr[root[1]]) :
			root[0] = arr[root[1]][root[2]]
			root[2] += 1

			max_ = max(max_,root[0])
		else:
			break
		replaceElement(heap,root)
	print("start : " + str(result[0])+" ; end : "+str(result[1])+" ; length : "+str(result[2]))
	



if __name__ == "__main__":
	arr = [[4,7,9,12,15],
		   [0,8,10,14,20],
		   [6,12,16,30,50]]
	smallestRange(arr)



