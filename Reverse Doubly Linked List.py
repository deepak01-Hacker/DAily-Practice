#User function Template for python3

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

def reverseDLL(head):
    tempHead = head
    prevs = None
    while(tempHead!=None):
        prevs = tempHead
        nexts = tempHead.next
        tempHead.next = tempHead.prev
        tempHead.prev = nexts
        tempHead = nexts
    return prevs
