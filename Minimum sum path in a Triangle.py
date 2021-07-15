
def minSumPath(A):

    dp = A[-1][:]

    for i in range(len(A)-2,-1,-1):
        for j in range(len(A[i])):
            dp[j] = A[i][j] + min(dp[j],dp[j+1])
        #print(dp)

    return dp[0]


if __name__ == "__main__":
    A =[[ 2 ],
        [3, 9 ],
       [1, 6, 7 ],
       [143,122,1323,1]]
    print(minSumPath(A))    
