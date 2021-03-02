#User function Template for python3

import heapq as hp

def minCost(a,n) :
    ans = 0
    jointer = [a[i] for i in range(n)]
    hp.heapify(jointer)
    while(len(jointer)>1):
        first_rope = hp.heappop(jointer)
        second_rope = hp.heappop(jointer)
        ans += first_rope+second_rope
        hp.heappush(jointer,first_rope+second_rope)
        
    return ans
        
