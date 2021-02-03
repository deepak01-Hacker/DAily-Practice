def smallestSubestWithMax(arr,n):
    arr.sort()
    sum_arr = sum(arr)
    temp_sum = 0
    ans_ = 0
    for i in range(n-1,-1,-1):
        ans += 1
        sum_arr -= arr[i]
        temp_sum += arr[i]
        if temp_sum > sum_arr:
            return ans
