def BadChar(pat,m):
    bad = [1]*256
    for i in range(m):
        bad[ord(pat[i])] = m-i-1
    bad[ord(pat[-1])] = m
    return bad

def BooyerMoore(pat,text):
    m = len(pat)
    n = len(text)
    badchar = BadChar(pat,m)
    i = 0 
    while(i <= n-m):
        j = m-1
        while(j >= 0 and text[i+j] == pat[j] ):
            j -= 1
        if j < 0:
            print(i,i+m)
            i += m
        else:
            i += badchar[ord(text[i+j])]


if __name__ == "__main__":
    text = "ABAABDABA"
    pat = "ABA"
    print(BooyerMoore(pat,text))
    
