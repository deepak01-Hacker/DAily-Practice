for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    arr.sort()
    temp = 0
    sum = 0
    n = len(arr)-1
    for i in range(len(arr)//2):
        if temp != 0:
            sum += temp-arr[i]
        sum += arr[n] - arr[i]
        temp = arr[n]
        n -= 1
    sum += temp-arr[0]
    
    print(sum)
