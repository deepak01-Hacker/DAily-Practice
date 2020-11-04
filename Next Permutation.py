def nextPermutation(arr,n):
    permuPoint = n-2
    for i in range(n-1,-1,-1):
        if arr[i] > arr[i-1]:
            break
    permuPoint = i
    minIndex = permuPoint
    mins = arr[permuPoint-1]
    for i in range(permuPoint+1,n,1):
        if arr[i] > mins and arr[i] <= arr[minIndex]:
            minIndex = i
    arr[permuPoint-1],arr[minIndex] = arr[minIndex],arr[permuPoint-1]
    arr[permuPoint:] = sorted(arr[permuPoint:])
    

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        nextPermutation(arr,n)
        print(*arr)
