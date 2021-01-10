#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    def copyList(self, head):
        tempHead = head
        while tempHead:
            next = tempHead.next
            tempHead.next = Node(tempHead.data)
            tempHead.next.next = next
            tempHead = next
        curr = head
        while (curr):
            if curr.arb:
                curr.next.arb = curr.arb.next
            curr = curr.next.next
        newHead = Node(0)
        copycurr = newHead
        curr = head
        while(curr):
            copycurr.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            copycurr = copycurr.next
        return newHead.next
        
