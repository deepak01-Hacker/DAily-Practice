#User function Template for python3

def isValid(arr,r,c,check):
    R = len(arr)
    C = R

    return r>= 0 and c >= 0 and r< R and c < C and arr[r][c] == 1 and check[r][c] != True

def path(arr,r,c,R,W,check,ans,paths):
    if isValid(arr,r,c,check) == False:
        return 0
    if r == R-1 and c == W-1:
        ans.append(paths)
        return 1
    check[r][c] = True
    if isValid(arr,r+1,c,check):
        paths += 'D' 
        path(arr,r+1,c,R,W,check,ans,paths)
        paths = paths[:-1]
    if isValid(arr,r,c-1,check):
        paths += 'L'
        path(arr,r,c-1,R,W,check,ans,paths)
        paths = paths[:-1]
    if isValid(arr,r,c+1,check):
        paths += 'R'
        path(arr,r,c+1,R,W,check,ans,paths)
        paths = paths[:-1]
    if isValid(arr,r-1,c,check):
        paths += 'U'
        path(arr,r-1,c,R,W,check,ans,paths)
        paths = paths[:-1]
    
    check[r][c] = False



def findPath(arr, n):
    ans = []
    paths = ''
    check = [[False for _ in range(n)] for _ in range(n)]
    path(arr,0,0,n,n,check,ans,paths)
    return ans 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1

        result = findPath(matrix, n[0])
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
