def spiral(matrix,n,m):
    rowStart = 0
    colStart = 0
    while(rowStart < n and colStart < m ):
        
        for i in range(colStart,m):
            print(matrix[rowStart][i],end=" ")
        rowStart += 1
        for i in range(rowStart,n):
            print(matrix[i][m-1],end=" ")
        m -= 1
        
        if (rowStart < n):
        
            for i in range(m-1,colStart-1,-1):
                print(matrix[n-1][i],end=" ")
            n -= 1
        if (colStart<m):
            for i in range(n-1,rowStart-1,-1):
                print(matrix[i][colStart],end=" ")
            colStart += 1    
        
            
if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        matrix = []
        for i in range(0,len(arr),m):
            matrix.append(arr[i:i+m+1])
        spiral(matrix,n,m)
        print()
