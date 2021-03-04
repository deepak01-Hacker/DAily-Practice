#User function Template for python3

class Solution:
    def util(self,arr,B,ans,result):
        if B < 0:
            return 
        if B == 0:
            temp = [val for val in ans]
            result.append(temp)
            return 
        for val in arr:
            if val > B:
                return 
            if (ans == [] or (ans != [] and ans[-1] <= val)):
                ans.append(val)
                self.util(arr,B-val,ans,result)
                ans.pop()
        return 

    
    def combinationalSum(self,a, s):
        ans = []
        result = []
        self.util(a,s,ans,result)
        return result
