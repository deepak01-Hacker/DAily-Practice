#User function Template for python3

def isSafe(grid,row,col,num):
    for i in range(0,9):
        if grid[row][i] == num:
            return False
            
    for j in range(0,9):
        if grid[j][col] == num:
            return False
    
    startRow = row - (row % 3)
    startCol = col - (col%3)

    for i in range(0,3):
        for j in range(0,3):
            if grid[i+startRow][j+startCol] == num:
                return False
    return True


def isEmptyBlock(grid,l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def sudokuSolver(grid):

    l = [0,0]
    if isEmptyBlock(grid,l) == False:
        return True

    row = l[0]
    col = l[1]
    for num in range(1,10):

        if isSafe(grid,row,col,num):

            grid[row][col] = num

            if sudokuSolver(grid):
                return True

            grid[row][col] = 0
            
    return False


def SolveSudoku(grid):
    return sudokuSolver(grid)
    
    
def printGrid(arr):
    
    for row in range(0,9):
        for col in range(0,9):
            print(arr[row][col],end=" ")
    print()
    
    
    # Your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
            
        if(SolveSudoku(grid)==True):
            printGrid(grid)
        else:
            print("No solution exists")
        t = t-1

# } Driver Code Ends
