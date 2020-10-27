def meadin(arr1,arr2,n,m):
    result = [-1,-1]
    index = 0
    mid = (n+m)//2
    arr1_p = 0
    arr2_p = 0
    val = 0
    while(arr1_p < n and arr2_p < m):
        if arr1[arr1_p] < arr2[arr2_p]:
            val = arr1[arr1_p]
            arr1_p += 1
        else:
            val = arr2[arr2_p]
            arr2_p+= 1
        if index == mid-1:
            result[0] = val
        elif index == mid:
            result[1] = val
            return (result[1]+result[0])//2
        index += 1
    if -1 in result:
        while(arr1_p < n):
            val = arr1[arr1_p]
            if index == mid-1:
                result[0] = val
            elif index == mid:
                result[1] = val
                (result[1]+result[0])//2
            arr1_p+=1
            index += 1
        while(arr2_p < m):
            val = arr2[arr2_p]
            if index == mid-1:
                result[0] = val
            elif index == mid:
                result[1] = val
                return (result[1]+result[0])//2
            arr2_p+=1
            index += 1      
if __name__ == "__main__":
    for _ in range(int(intput)):
        arr1 = list(map(int,input().rstrip().split(" ")))
        arr2 = list(map(int,input().rstrip().split(" ")))
        print(meadin(arr1,arr2,len(arr1),len(arr2)))
