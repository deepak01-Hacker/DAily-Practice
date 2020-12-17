#User function Template for python3

class Solution:
    def inSequence(self, A, B, C):
        if A == B :
            return 1
        elif (A > 0 and B < 0 and C > 0) or (C == 0):
            return 0
        s = (B - A + C)
        if s%C == 0 and s//C > 0:
            return 1
        else:
            return 0
