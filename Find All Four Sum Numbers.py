#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required

def fourSum(arr, k):
    ans = []
    arr.sort()
    n = len(arr)
    i = 0 
    j = 1
    while(i < n-3):
        j = i+1
        while( j >= i+1 and j<n-2):
            left = j+1
            right = n-1
            while(left < right):
                sum = arr[i]+arr[j]+arr[left]+arr[right]
                if  sum == k:
                    ans.append([arr[i],arr[j],arr[left],arr[right]])
                    leftValue = arr[left]
                    while(left < n and arr[left] == leftValue):
                        left += 1
                    rightValue = arr[right]
                    while(right > j+1 and arr[right] == rightValue):
                        rightValue -= 1
                elif sum < k:
                    left += 1
                else:
                    right -= 1
            leftright = arr[j]
            while(j < n-2 and arr[j] == leftright):
                j += 1
        leftleft = arr[i]
        while(i<n-3 and arr[i] == leftleft):
            i += 1
    return ans
                
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ans=fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends
