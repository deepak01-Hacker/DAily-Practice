def maximumMeetings(n,start,end):
    
    l = [[start[i],end[i],i] for i in range(n)]

    l.sort(key = lambda x : x[1])

    ans = 1

    key = l[0][1]
    for i in range(1,n):
        if l[i][0] > key:
            ans += 1
            key = l[i][1]
    return ans
    
