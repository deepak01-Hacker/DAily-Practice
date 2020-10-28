class Solution(object):
    
    def binarySearch(self,arr,tr):
        if len(arr)>0:
            left = 0
        else:
            return False
        right = len(arr)-1
        while(left<=right):
            mid = left+(right-left)//2
            if arr[mid] == tr:
                return True
            elif arr[mid] < tr:
                left = mid+1
            else:
                right = mid-1
        return False
        
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if len(matrix[i]) > 0 and matrix[i][0] <= target and matrix[i][-1] >= target:
                if self.binarySearch(matrix[i],target):
                    return True
                else:
                    return False
            elif len(matrix[i]) == 0:
                continue
            elif matrix[i][0] > target:
                return False
            elif matrix[i][0] == target:
                return False
        return False
