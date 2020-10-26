def ans(arr,n,sum):
    mins_len = n
    left = 0
    len_count = 0
    temp_sum = 0
    for right in range(n):
        temp_sum += arr[right]
        len_count+= 1
        while(temp_sum > sum and left <= right):
            mins_len = min(mins_len,len_count)
            temp_sum -= arr[left]
            left += 1
            len_count -= 1
    return mins_len
    
if __name__=="__main__":
    for _ in range(int(input())):
        n,sum = map(int,input().rstrip().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        print(ans(arr,n,sum))
