def threeWayPartitioning(arr,low,high,length):
    i = 0 
    start = 0
    end = length
    while(i<=end):
        if arr[i] < low:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            i += 1
            start += 1
        elif arr[i] > high:
            temp = arr[i]
            arr[i] = arr[end]
            arr[end] = temp
            end -= 1
        else:
            i += 1
    return arr


if __name__ == "__main__":
    arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    low ,high = 14,20
    print(threeWayPartitioning(arr,low,high,len(arr)-1))
