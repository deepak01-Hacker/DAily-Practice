def ans(arr,n,k):
    window = 0
    for i in range(n):
        if arr[i]<=k:
            window += 1
    mins = n
    temp_window = 0
    for i in range(0,window):
        if arr[i] > k:
            temp_window += 1
    mins = temp_window
    for j in range(1,n-window+1):
        if arr[j-1] > k:
            temp_window -= 1
        if arr[j+window-1] > k:
            temp_window += 1
        mins = min(temp_window,mins)
    return mins
        
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        k = int(input())
        print(ans(arr,n,k))
