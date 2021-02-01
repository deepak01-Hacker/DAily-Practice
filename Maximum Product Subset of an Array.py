
def maximumProductSum(arr,n):
    if n == 1:
        return a[0]
    
    max_neg = -999999999999
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(n):

        if arr[i] == 0:
            count_zero += 1
            continue

        if arr[i]<0:
            count_neg += 1
            max_neg = max(max_neg,arr[i])
        
        prod = prod *arr[i]
    
    if count_zero == n:
        return 0
    
    if count_neg & 1 :# check number is even or odd

        if count_neg == 1 and count_zero > 0 and count_zero + count_neg == n:
            return 0

        prod = prod // max_neg

    return prod
