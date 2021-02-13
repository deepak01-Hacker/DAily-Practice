def isPalindrome(string: str, 
                 low: int, high: int): 
    while low < high: 
        if string[low] != string[high]: 
            return False
        low += 1
        high -= 1
    return True


def utilallpalindrome(allpart,copyPal,start,n,st):

    if start >= n:
        
        x = copyPal.copy()

        allpart.append(x)

        return 
    for i in range(start,n):
        if isPalindrome(st,start,i):
            copyPal.append(st[start:i+1])

            utilallpalindrome(allpart,copyPal,i+1,n,st)

            copyPal.pop()


def allpalindrome(st):
    n = len(st)

    allpart = []
    
    copyPal = []

    utilallpalindrome(allpart,copyPal,0,n,st)

    for i in range(len(allpart)):
        for j in range(len(allpart[i])):
            print(allpart[i][j],end=" ")
        print()


if __name__ == "__main__":
    st = "nitin"
    allpalindrome(st)
