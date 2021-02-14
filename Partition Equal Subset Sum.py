class Solution:
    def util(self,arr,N,sum_):
        if sum_ == 0:
            return True
        if N == -1:
            return False
        return self.util(arr,N-1,sum_-arr[N]) or self.util(arr,N-1,sum_)
        
    def equalPartition(self, N, arr):
        sum_ = sum(arr)
        if 1&sum_:
            return 0
        sumDivide = sum_//2
        if self.util(arr,N-1,sumDivide):
            return 1
        return 0
