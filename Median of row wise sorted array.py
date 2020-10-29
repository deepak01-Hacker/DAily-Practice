import sys
from bisect import bisect_right as upper_bound

def binaryMedian(m,r,c):
	min = sys.maxsize
	max = -sys.maxsize 
	for i in range(0,r):
		if m[i][0] < min:
			min = m[i][0]
		if m[i][c-1] > max:
			max = m[i][c-1]
	
	median = (r*c+1)//2

	while(min<max):
		mid = min+(max-min)//2
		place = [0];

		for i in range(r):
			j = upper_bound(m[i],mid)
			place[0] = place[0]+j
		if place[0] < median :
			min = mid + 1
		else:
			max = mid 
	return min
if __name__ == "__main__":
	matrix = [[1,3,5],
			 [2,6,9],
			 [3,6,9]]	
	print(binaryMedian(matrix,r,c))	
