def TheDoubleHelix(arr1,arr2,n1,n2):
    ans = 0
    sum1 = 0
    sum2 = 0
    i = 0
    j = 0
    while(i<n1 and j < n2):
        if arr1[i] == arr2[j]:
            sum1 += arr1[i]
            sum2 += arr2[j]
            ans += max(sum1,sum2)
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        else:
            sum2 += arr2[j]
            j += 1
    while(i < n1):
        sum1 += arr1[i]
        i += 1
    while(j < n2):
        sum2 += arr2[j]
        j += 1
    ans += max(sum1,sum2)
    return ans
        


if __name__ == "__main__":
    arr1 = [3,5,7,9,20,25,30,40,55,56,57,60,62]
    arr2 = [1,4,7,11,14,25,44,47,55,57,100]
    print(TheDoubleHelix(arr1,arr2,len(arr1),len(arr2)))
