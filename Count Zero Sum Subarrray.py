#User function Template for python3

def findSubArrays(arr,n):
    hash = {}
    temp = 0
    for i in range(n):
        temp += arr[i]
        try:
            hash[temp] += 1
        except:
            hash[temp] = 1
    ans = 0
    for k in hash:
        n = hash[k]
        if k != 0:
            n -= 1
        ans += (n*(n+1))//2
    return ans
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().strip().split(' ')]
        print(findSubArrays(A,N))
        
                
