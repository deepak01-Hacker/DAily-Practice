#Transform One string to other string

"""
Given two strings A and B, the task is to convert A to B if possible. The only operation allowed is to put any character from A 
and insert it at front. Find if it’s possible to convert the string. If yes, then output minimum no. of operations required for transformation.
"""

def isvalid(st1,st2):
    count = [0]*256
    for st in st1:
        count[ord(st)] += 1
    for st in st2:
        count[ord(st)] -= 1
    if sum(count) == 0:
        return True
    return False

def Transform(st1,st2):
    if isvalid(st1,st2):
        res = 0
        i = len(st1)-1
        j = len(st2)-1
        while(i>=0):
            
            while i>=0 and st1[i] != st2[j] :
                i -= 1
                res += 1
            if i>=0:
                i -= 1
                j -= 1
        return res


    else:
        return False
