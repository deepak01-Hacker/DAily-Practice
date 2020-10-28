import heapq

class Node:

    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

def prints(root,strs):
    if root is None:
        return 
    if root.data!='$':
        print(root.data,strs)
    prints(root.left,strs+'0')
    prints(root.right,strs+'1')


def huffmanCoding(datas,freqs,n):
    heap = []
    heapq.heapify(heap)
    for i in range(n):
        temp = Node(datas[i],freqs[i])
        heapq.heappush(heap,[freqs[i],temp])
    while(len(heap)!=1):
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        temp = Node('$',left[0]+right[0])
        temp.left = left[1]
        temp.right = right[1]
        heapq.heappush(heap,[left[0]+right[0],temp])
    root = heapq.heappop(heap)
    prints(root[1],'')

if __name__ == "__main__":
    arr = ['a','b','c','d','e','f']
    freq = [5,9,12,13,16,45]

    huffmanCoding(arr,freq,len(freq))
