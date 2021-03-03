
import heapq

def solve(arr, n):
    heapq.heapify(arr)
    x1 = ""
    x2 = ""
    while(n>1):
        topSmall = heapq.heappop(arr)
        secondSmall = heapq.heappop(arr)
        x1 += str(topSmall)
        x2 += str(secondSmall)
        
        n -= 2
    if n == 1:
        x1 += str(arr[0])
    ans = int(x1)
    ans += int(x2)
    return ans
