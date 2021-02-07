
import heapq

def isPossible(st):
    n = len(st)
    map = {}
    for i in range(len(st)):
        try:
            map[st[i]] += 1
        except:
            map[st[i]] = 1
    heap = []
    for i in map.keys():
        heap.append([-map[i],i])
    heapq.heapify(heap)
    st1 = ""
    prev = [0,"#"]
    while(len(heap)):
        
        new = heapq.heappop(heap)
        st1 += new[1]
        print(new,prev)
        new[0] += 1
        
        if prev[0] < 0:
            heapq.heappush(heap,prev)
        prev = new
    if n != len(st1):
        return 0
    return 1
        
