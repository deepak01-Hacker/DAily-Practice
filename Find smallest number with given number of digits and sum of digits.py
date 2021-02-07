        

#User function Template for python3
class Solution:
    def smallestNumber(ob,S,D):
        ans = [0 for _ in range(D)]
        temp_sum = 9*D
        if S > temp_sum:
            return "-1"
        S -= 1
        for i in range(D-1,0,-1):
            if S > 9:
                ans[i] = 9
                S -= 9
            else:
                ans[i] = S
                S = 0
        ans[0] = S+1
        ans1 = ""
        for i in range(D):
            ans1+=str(ans[i])
        return ans1
            
        
