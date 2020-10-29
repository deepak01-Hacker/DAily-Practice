global n 
n = 4


def issafe(board,row,col):
	for i in range(col):
		if board[row][i] == 1:
			return False 
	for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
		if board[i][j] == 1:
			return False

	for i,j in zip(range(row,n,1),range(col,-1,-1)):
		if board[i][j] == 1:
			return False
	return True

def help(board,col):
	if col >= n:
		return True

	for i in range(n):
		if issafe(board,i,col):
			board[i][col] = 1

			if help(board,col+1) == True:
				return True
			
			board[i][col] = 0
	return False

def solveNq():
	board = [[0 for _ in range(n)] for _ in range(n)]
	
	if help(board,0):
		print(*board)
	else:
		print("Answer is not exist")

if __name__ == "__main__":
	solveNq()
