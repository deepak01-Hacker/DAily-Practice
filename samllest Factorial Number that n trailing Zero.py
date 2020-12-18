#User function Template for python3

class Solution:
    def countZero(self,mid ,n ):
        ans = 0
        p = 5
        while(p <= mid):
            ans += mid//p
            p *= 5
        return (ans >= n)
        
    def findNum(self, n):
        if n == 1:
            return 5
        low = 0
        high = 5*n
        while(low < high):
            mid = (low+high) >> 1
            if self.countZero(mid,n):
                high = mid
            else:
                low = mid+1
        return low
