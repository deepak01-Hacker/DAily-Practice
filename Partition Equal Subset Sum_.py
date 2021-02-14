class Solution:
    def util(self,arr,start,N,sum_):
        if sum_ == 0:
            return True
        if sum_< 0:
            return False
        if start > N:
            return False
        for i in range(start,N):
            sum_ -= arr[i]
            if self.util(arr,i+1,N,sum_):
                return True
            sum_ += arr[i]
        return False 

        
    def equalPartition(self, N, arr):
        sum_ = sum(arr)
        if 1&sum_:
            return 0
        sumDivide = sum_//2
        if self.util(arr,0,N-1,sumDivide):
            return 1
        return 0
