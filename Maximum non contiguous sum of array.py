def ans(arr,n):
    n += 1
    dp = [0]*(n)
    dp[0] = 0
    dp[1] = arr[0]
    for i in range(2,n):
        dp[i] = max(dp[i-2]+arr[i-1],dp[i-1])
    return dp[n-1]
    
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(ans(arr,n))
