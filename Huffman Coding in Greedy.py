class Node:
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

import heapq


def printHuffman(roots,str):
    if roots is None:
        return 
    if roots.data != "$":
        print(str,end=" ")
    printHuffman(roots.left,str+"0")
    printHuffman(roots.right,str+"1")

def huffmanEncoding(alph,freqs):
    heap = []
    heapq.heapify(heap)
    for i in range(len(freqs)):
        temp = Node(alph[i],freqs[i])
        heapq.heappush(heap,(freqs[i],temp))
    while(len(heap)!=1):
        leftr = heapq.heappop(heap)
        rightr = heapq.heappop(heap)
        
        temp = Node("$",leftr[1].freq + rightr[1].freq)
        temp.left = leftr[1]
        temp.right = rightr[1]
        heapq.heappush(heap,(temp.freq,temp))
        
    root = heapq.heappop(heap)
    roots = root[1]
    printHuffman(roots,"")



if __name__ == "__main__":
    for _ in range(int(input())):
        alph = input()
        freq = list(map(int,input().rstrip().split(" ")))
        huffmanEncoding(alph,freq)
        
