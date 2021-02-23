def sumMinimumMax(arr,k):
	

	increse = []
	decrease = []
	sum = 0
	for i in range(k):
		while(len(increse) > 0 and arr[increse[-1]] >= arr[i]):
			increse.pop()
		while(len(decrease)>0 and arr[decrease[-1]] <= arr[i]):
			decrease.pop()
		increse.append(i)
		decrease.append(i)
	print(increse,decrease)
	
	for i in range(k,len(arr)):
		
		sum += arr[increse[0]]+arr[decrease[0]]

		while(len(increse) > 0 and increse[0] <= i-k):
			increse.pop(0)
		while(len(decrease) > 0 and decrease[0] <= i-k):
			decrease.pop(0)


		while(len(increse) >0 and arr[increse[-1]] >= arr[i]):
			increse.pop()
		while(len(decrease)>0 and arr[decrease[-1]] <= arr[i]):
			decrease.pop()

		increse.append(i)
		decrease.append(i)

	sum += arr[increse[0]]+arr[decrease[0]]
	print(sum)
