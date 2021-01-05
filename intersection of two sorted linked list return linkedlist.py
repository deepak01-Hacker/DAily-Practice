#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

def findIntersection(head1,head2):
    prev = None
    head = None
    while(head1 and head2):
        if head1.data == head2.data:
            if head is None:
                head = Node(head1.data)
                prev = head
            else:
                prev.next = Node(head1.data)
                prev = prev.next
            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            head1 = head1.next
        else:
            head2 = head2.next
    return head

