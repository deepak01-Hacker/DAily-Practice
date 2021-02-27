import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        map = {}
        for char in S:
            try:
                map[char] += 1
            except:
                map[char] = 1
        ans = ""
        heap = []
        heapq.heapify(heap)
        for t in map.keys():
            heapq.heappush(heap,[-map[t],t])
        map.clear()
        while(len(heap) > 1):
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            ans += first[1]
            ans += second[1]
            
            first[0] += 1
            second[0] += 1
            
            if first[0] < 0:
                heapq.heappush(heap,first)
            if second[0] < 0:
                heapq.heappush(heap,second)
        
        if heap == []:
            return ans
    
        first = heapq.heappop(heap)
        ans += first[1]
        first[0] += 1
        if first[0] < 0:
                heapq.heappush(heap,first)
        if heap == []:
            return ans
        return ""
