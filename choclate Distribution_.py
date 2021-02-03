def distribution(arr,n,m):
    arr.sort()
    mins = 10**7
    for i in range(n-m+1):
        mins = min(mins,arr[i+m-1]-arr[i])
    return mins
    
if __name__=="__main__":    
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        m = int(input())
        print(distribution(arr,n,m))
