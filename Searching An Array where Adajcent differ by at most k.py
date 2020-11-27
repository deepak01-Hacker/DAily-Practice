def searchingArray(arr,n,k,x):
    i = 0
    while(i<n):
        if arr[i] == x:
            return i
            
        i = i+max(1,int(abs(arr[i]-x)/k))
    return -1

if __name__ == "__main__":
    for _ in range(int(input())):
        n,k = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        x   = int(input())
        print(searchingArray(arr,n,k,x))
