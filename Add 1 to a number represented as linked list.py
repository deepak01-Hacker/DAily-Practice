#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

def addOne(head):
    number = ''
    temp = head
    while(temp):
        number += str(temp.data)
        temp = temp.next
    resultNumber = str(int(number)+1)
    if len(number) < len(resultNumber):
        newHead = Node(resultNumber[0])
        newHead.next = head
        head = newHead
    pt = head
    i = 0
    while(pt):
        pt.data = int(resultNumber[i])
        i += 1
        pt = pt.next
    return head
        
