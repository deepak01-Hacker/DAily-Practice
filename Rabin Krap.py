#Python3
#Rabin Krap Algorithm for Patteren Matching

def match(text,patteren,left):
    for i in range(len(patteren)):
        if patteren[i] != text[i+left]:
            break
    if i == len(patteren)-1:
        return True
    return False

def windowCheck(t,p,hash_p,hash_t):
    left = 0
    len_p = len(p)
    for i in range(len_p,len(t),1):
        hash_t = hash_t - (ord(text[left])-64)
        hash_t = hash_t//3
        hash_t += (ord(text[i])-64) *(3**(len_p-1))
        left += 1 
        if hash_p == hash_t:
            if match(t,p,left):
                return True
    return False

def RabinKrap(text,patteren):
    hash_t = 0
    hash_p = 0
    for i in range(len(patteren)):
        hash_p += (ord(patteren[i])-64)*(3**i)
        hash_t += (ord(text[i])-64)*(3**i)
    if hash_p == hash_t:
        if match(text,patteren,0):
            return True
    return windowCheck(text,patteren,hash_p,hash_t)



if __name__ == "__main__":
    text = input()  #MAin String
    patteren = input()   #Patteren 
    print(RabinKrap(text,patteren))
