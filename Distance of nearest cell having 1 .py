


def minDistance(mat,R,C):
	

	#we use here BFS

	R = len(mat)
	C = len(mat[0])

	maxSize = 999999999

	ans = [[maxSize for _ in range(C)] for _ in range(R)]

	queue = []

	for i in range(R):
		for j in range(C):
			if mat[i][j] == 1:
				queue.append([i,j])
	
	dis = 0
	row_val = [-1,1,0,0]
	col_val = [0,0,-1,1]
	while(queue):
		size = len(queue)
		for _ in range(size):
			pairOneContain = queue.pop(0)
			i = pairOneContain[0]
			j = pairOneContain[1]

			ans[i][j] = min(dis,ans[i][j])

			for k in range(len(row_val)):
				r = i + row_val[k]
				c = j + col_val[k]
				if (r >= 0 and c>=0 and r<R and c < C and ans[r][c] == maxSize):
					queue.append([r,c])
		dis += 1
	return ans

		

if __name__ == "__main__":
	mat = [[1,0,0,1],
		   [0,0,1,1],
		   [1,1,0,0]]

	print(minDistance(mat,len(mat),len(mat[0])))

