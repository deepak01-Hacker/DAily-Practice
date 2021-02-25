

rowNum = [-1,0,0,1]
colNum = [0,-1,1,0]

def isSafe(mat,visited,x,y):

	if mat[x][y] == 0 or visited[x][y]:
		return False
	return True

def isValid(x,y,R,C):
	return x < R and y < C and x>=0 and y>=0

def preprocess(mat,R,C):
	for i in range(R):
		for j in range(C):
			if mat[i][j] == 0:
				for k in range(4):
					if isValid(i+rowNum[k],j+colNum[k],R,C):
						mat[i+rowNum[k]][j+colNum[k]] = -1
	for i in range(R):
		for j in range(C):
			if mat[i][j] == -1:
				mat[i][j] = 0

def findShortestPathUtil(mat,visited,i,j,Dist,curr):
	if J == C-1:
		Dist[0] = min(Dist[0],curr)

	if curr>Dist[0]:
		return
	
	visited[i][j] = 1

	for k in range(4):
		if isValid(i+rowNum[k],j+colNum[k],R,C) and isSafe(mat,visited,i+rowNum[k],j+colNum[k]):
			findShortestPathUtil(mat,visited,i+rowNum[k],j+colNum[k],Dist,curr+1)

	visited[i][j] = 0

def findShortestPath(mat,R,C):

	Dist = [9999999999]

	preprocess(mat,R,C)

	for i in range(R):
		
		visited = [[0 for _ in range(C)] for _ in range(R)]

		findShortestPathUtil(mat,visited,i,0,Dist,0)

		if Dist[0] == C-1:
			break
	
	
	print(Dist)
	
