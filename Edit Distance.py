class Solution:
	def editDistance(self, s, t):
	    n = len(s)
	    m = len(t)
	    
	    dp = [[ 0 for _ in range(m+1)] for _ in range(n+1)]
	    
	    for i in range(n+1):
	        for j in range(m+1):
	            if i == 0 or j == 0:
	                dp[i][j] = j if i == 0 else i
	            elif s[i-1] == t[j-1]:
	                dp[i][j] = dp[i-1][j-1]
	            else:
	                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
	    return dp[n][m]



#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends
