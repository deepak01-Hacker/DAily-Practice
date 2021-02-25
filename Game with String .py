#User function Template for python3
import heapq

class Solution:
    def minValue(self, s, k):
        map = {}
        for char in s:
            try:
                map[char] += 1
            except:
                map[char] = 1
        heap = []
        
        for value in map.keys():
            heap.append(-map[value])
        heapq.heapify(heap)
        while(k>0):
            temp = heapq.heappop(heap)
            temp += 1
            k -= 1
            heapq.heappush(heap,temp)
        sum = 0
        for i in range(len(heap)):
            sum += heap[i]**2
        return sum
            
