def ans(arr,n):
    i = 0
    j = n-1
    op =0
    while(i<j):
        if arr[i] == arr[j]:
            i += 1
            j -= 1
            continue
        if arr[i] < arr[j]:
            arr[i+1] += arr[i]
            op += 1
            i += 1
        else:
            arr[j-1] += arr[j]
            op += 1
            j -= 1
            
    return op
if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))     
        print(ans(arr,n))
