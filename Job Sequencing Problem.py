#User function Template for python3


def JobScheduling(Jobs,n):
    
    Jobs.sort(key = lambda x : x.profit,reverse=True)
    
    selected = [0]*100
    ans = [0,0]
    for i in range(n):
        for j in range(min(n,Jobs[i].deadline)-1,-1,-1):
            if selected[j] == 0:
                selected[j] = 1
                ans[1] += Jobs[i].profit
                ans[0] += 1
                break
    return ans
