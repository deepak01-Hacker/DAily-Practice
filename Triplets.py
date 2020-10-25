def triplets(arr,n,k):
    arr.sort()
    index = 0
    while(index<=n-2):
        for i in range(index+1,n-1):
            if arr[i]<k:
                for j in range(i+1,n):
                    print(arr[index],arr[i],arr[j])
                    if arr[j] > k:
                        break
                    if (arr[index]+arr[i]+arr[j]) == k:
                        return True
            else:
                break
        index += 1
    return False
    
if __name__=="__main__":
    n,k = 6,13
    arr = [1 ,4, 45 ,6 ,10 ,8]
    if triplets(arr,n,k):
        print("1")
    else:
        print("0")
