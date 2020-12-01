def countTriplets(arr,n,x):
    arr.sort()
    count = 0
    for i in range(n-2):
        l = i+1
        r = n-1
        while(l<r):
            sum = arr[i]+arr[l]+arr[r]
            if sum >= x:
                r -= 1
            else:
                count += (r-l)
                l += 1
    return count

if __name__ == "__main__":
    arr = [5,1,3,4,7]
    n = 5
    x = 12
    print(countTriplets(arr,n,x))
