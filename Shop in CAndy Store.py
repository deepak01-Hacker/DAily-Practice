def ans(n,k,arr):
    arr.sort()
    i = 0
    min_ = 0
    while(i<n):
        min_ += arr[i]
        i += 1
        n -= k
    max_ = 0
    index = 0
    n = len(arr)-1
    while(n>=index):
        max_ += arr[n]
        n -= 1
        index+=k
    print(min_,max_)

if __name__ == "__main__":
    for _ in range(int(input())):
        n,k = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        ans(n,k,arr)
