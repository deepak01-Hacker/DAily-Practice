#Kuth Morris Patt (Don;t Mind My spelling Mistake)
def preprocess(prefix,pat,M):
    prefix[0] = 0
    len = 0 
    i = 1
    while(i<M):
        if pat[i] == pat[len]:
            len += 1
            prefix[i] = len
            i += 1
        elif len != 0:
            len = prefix[len-1]
        else:
            prefix[i] = 0
            i += 1

def KMP(text,pat):
    M = len(pat)
    prefix = [0]*M
    preprocess(prefix,pat,M)
    i = 0
    j = 0
    while(i<len(text)):
        if text[i] == pat[j]:
            i += 1
            j += 1
        elif j != 0:
            j = prefix[j-1]
        else:
            i += 1
        if j == M:
            return (i-M,i-1)


if __name__ == "__main__":
    text = "abdebcabc"
    pat = "abc"
    print(KMP(text,pat))
