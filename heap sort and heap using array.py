
def heapify(arr,i,n):

	largest = i
	left = 2 * i + 1
	right= 2 * i + 2

	if l < n and arr[largest] < arr[left]:
		largest = left
	if r < n and arr[largest] < arr[right]:
		largest = right
	
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr,largest,n)


def buildHeap(arr):

	n = len(arr)

	startIndex = (n//2) - 1

	for i in range(startIndex-1,-1,-1):
		heapify(arr,i,n)

	#if Sort using heap then :

	for i in range(n-1,0,-1):
		arr[i],arr[0] = arr[0],arr[i]
		heapify(arr,i,n)
	
