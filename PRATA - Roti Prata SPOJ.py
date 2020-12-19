#Simple AnsWer of Roti Prata in Python
If you have any doubt mail me a9649060356@gmail.com


Question Link : https://www.spoj.com/problems/PRATA/

------------------------------------------------------------------------------------------------------------------------------------------


def maxTime(ar,P):
    total = 0
    for i in range(1,(P+1)):
        total += ar*i
    return total

def isItsPossibleinThisTime(arr,n,P,mid):
    c = 0
    for i in range(n):
        cnt = 0
        Time = mid
        perata = arr[i]
        while(Time>0):
            Time -= perata
            if (Time>=0):
                cnt += 1
                perata += arr[i]
        c += cnt
        if (c>=P):
            print(mid)
            return True
    return False
            

def minimumTime(arr,P,n):
    arr.sort()
    low = 1
    high = maxTime(arr[-1],P)
    ans = high
    while(low<=high):
        mid = (low+high)//2 
        if isItsPossibleinThisTime(arr,n,P,mid):
            ans = min(ans,mid)
            high = mid-1
        else:
            low = mid+1
    return ans



if __name__ == "__main__":
    arr = [1,2,3,4]
    Parrata = 10
    n = 4
    print(minimumTime(arr,Parrata,n))
