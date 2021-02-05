def checkFire(H,A):
    if (H-20 >= 0) and (A+5 >= 0):
        return True
    return False

def checkAir(H,A):
    if (H+3 >= 0) and (A+2 >= 0):
        return True
    return False

def checkWater(H,A):
    if (H-5 >= 0) and (A-10 >= 0):
        return True
    return False

def whenDie(H,A): # Greedy
    n = 0
    p = ''
    while(True):
        if p != 'a' and checkAir(H,A):
            H += 3
            A += 2
            p = 'a'
        elif p != 'w' and checkWater(H,A) and H < A:
            print(H,A,'w')
            H -= 5
            A -= 10
            p = 'w'
        elif p != 'f' and checkFire(H,A) and H > A:
            print(H,A,'f')
            H -= 20
            A += 5     
            p = 'f'
        else:
            break 
        n += 1
    print(n)

def whenDiePro(H,A,arr,pre): #Recrsion and not efficient 
    """
    20 8
    23 10
    3, 5
    5,7
    0,

    0,3
    3,5
    """
    if H<0 or A < 0:
        return 0
    print(H,A)
    if pre == 'a':
        return max((whenDiePro(H-5,A-10,arr,'w')+1 if checkWater(H,A) else 0), (whenDiePro(H-20,A+5,arr,'f')+1 if checkFire(H,A) else 0))
    elif pre == 'w':
        return max((whenDiePro(H+3,A+2,arr,'a')+1 if checkAir(H,A) else 0), (whenDiePro(H-20,A+5,arr,'f')+1 if checkFire(H,A) else 0))
    else:
        return max((whenDiePro(H-5,A-10,arr,'w')+1 if checkWater(H,A) else 0), (whenDiePro(H+3,A+2,arr,'a')+1 if checkAir(H,A) else 0))



if __name__ == "__main__":
    arr = [0]
    ans = 1

    print(whenDiePro(4+3,4+2,arr,'a'))

