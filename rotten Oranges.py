class Solution:
    
	def orangesRotting(self, grid):
		
		
		queue = []
		ones = 0
		
		for i in range(len(grid)):
		    for j in range(len(grid[i])):
		        if grid[i][j] == 2:
		            queue.append([i,j]) 
                elif grid[i][j] == 1:
                    ones += 1
        
        ans = 0
        while(queue):
            size = len(queue)
		    if ones<=0:
		        return ans
		    ans += 1
		    for _ in range(size):
		        i = queue[0][0]
		        j = queue[0][1]
		        queue.pop(0)
		        
		        
		        if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    ones -= 1
                    queue.append([i-1,j])
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    ones -= 1
                    queue.append([i+1,j])
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    ones -= 1
                    queue.append([i,j-1])
                if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
		            ones -= 1
                    queue.append([i,j+1])
                
        return -1
		    
		        
		            
		        



#{ 
#  Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends
