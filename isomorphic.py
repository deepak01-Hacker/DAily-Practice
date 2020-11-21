#Check the two strings are isomorphics if yes then return True else return False

#User function Template for python3
def preprocessing(st1):
    match = [0]*27
    t = 1
    newst = ""
    for i in range(len(st1)):
        if match[ord(st1[i])-ord('a')] == 0:
            match[ord(st1[i])-ord('a')] = t
            t += 1
            
        newst += str(match[ord(st1[i])-ord('a')])

    return newst


def areIsomorphic(str1,str2):
    k1 = preprocessing(str1)
    k2 = preprocessing(str2)
    return k1 == k2
