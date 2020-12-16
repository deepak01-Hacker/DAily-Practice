#weighted Job Scheduling in o(nlogn)

class job:
    def __init__(self,start,finish,profit):
        self.start = start
        self.finish = finish
        self.profit = profit

def binarysearch(Job,index):
    low = 0
    high = index - 1
    while(low <= high):
        mid = (low+high)//2
        if Job[mid].finish <= Job[index].start:
            if Job[mid+1].finish <= Job[index].start:
                low = mid+1
            else:
                return mid
        else:
            high = mid-1
    return -1


def schedule(Job):
    n = len(Job)
    Job = sorted(Job,key = lambda J:J.finish)

    table = [0 for _ in range(n)]

    table[0] = Job[0].profit
    for i in range(1,n):
        inclprof = Job[i].profit
        l = binarysearch(Job,i)
        if (l != -1):
            inclprof += table[l]
        table[i] = max(inclprof,table[i-1])

    return table[n-1]

if __name__ == "__main__":
    Job = [job(1,2,50),
           job(3,5,20),
           job(6,19,100),
           job(2,100,200)]
    print(schedule(Job))
    
