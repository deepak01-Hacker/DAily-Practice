#User function Template for python3

class Solution:
    
    def celebrity(self, M, n):
        a = 0
        b = n-1
        
        while(a<b):
            if M[a][b]:
                a += 1
            else:
                b -= 1
        for i in range(n):
            if i != a and (M[a][i] or M[i][a] == 0) :
                return -1
        return a
                
