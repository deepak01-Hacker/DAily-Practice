#User function Template for python3
def minimumPlatform(n,arr,dep):
    temp = [[dep[i],i] for i in range(n)]

    temp.sort(key=lambda x : x[0])

    ans = 0
    while(len(temp)):
        i = 0
        second_compare = temp[0][0]
        temp.pop(0)
        while(i<len(temp)):
            print(i)
            if arr[temp[i][1]] >= second_compare:
                t = temp.pop(i)
                print(second_compare)
                second_compare = t[0]
            else:
                i += 1
        ans += 1
    return ans
