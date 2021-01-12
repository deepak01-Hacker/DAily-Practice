#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''

def reverseLL(head):
    prev = None
    while(head):
        temp = head.next
        head.next = prev 
        prev = head
        head = temp
    return prev


def computes(head):
    curr = head
    maxNode = head
    while (curr and curr.next):
        if curr.next.data < maxNode.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
            maxNode = curr
    return head
    
def compute(head):
    head = reverseLL(head)

    head = computes(head)
    head = reverseLL(head)

    return head

    
