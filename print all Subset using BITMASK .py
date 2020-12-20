#Bit Masking 
def printAllsubArray(arr,n):
    total = 1<<n
    for mask in range(total):
        for i in range(n):
            f = 1<<i
            if ((mask&f) != 0):
                print(arr[i],end=" ")
                t = 0
        print()


if __name__ == "__main__":
    n = 4 
    arr = ['A','B','C','D']
    printAllsubArray(arr,n)
    
