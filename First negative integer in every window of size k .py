def firstnegativeInteger(arr,k):
	queue = []
	for i in range(k):
		if arr[i] < 0:
			queue.append([arr[i],i])
	end = k
	j = 1
	while(end<len(arr)):
		if queue != [] :
			print(queue[0][0],end=" ")
			if queue[0][1] < j:
				queue.pop(0)
		else:
			print(0,end=" ")
		if arr[end] < 0:
			queue.append([arr[end],end])
		end+= 1
		j += 1
	if queue == []:
	    print(0,end=" ")
	else:
	    print(queue[0][0],end=" ")

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        k = int(input())
        firstnegativeInteger(arr,k)
        print()
