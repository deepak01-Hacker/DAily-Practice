"""
    Code By    :  Deepak
    Contact us :  
"""

#Problem :- Find Minimum window that contain 


def hash_(st):
    return len(set(st))

def miniWindow(st):
    start_min = 0
    end_min = 10**5
    i = 0
    j = 0
    hash = hash_(st)
    print(hash)
    map = [0] *256
    len_ = len(st)
    temp_hash = 0
    while(i<=j and j <=len_ ):
        if temp_hash == hash:
            if j+1-i < end_min-start_min:
                start_min = i
                end_min = j
            map[ord(st[i])] -= 1
            if map[ord(st[i])] == 0:
                temp_hash -= 1
            i += 1
        elif j < len_:
            map[ord(st[j])] += 1
            if map[ord(st[j])] == 1:
                temp_hash += 1
            j += 1
        else:
            break
    for i in range(start_min+1,end_min):
        print(st[i],end="")
    print()



if __name__ == "__main__":
    for _ in range(1):
        st = "daaabded"
        miniWindow(st)
