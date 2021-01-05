#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def addLists(first, second):
    firstNumber = ''
    secondNumber = ''
    tempHead = first
    while(tempHead):
        firstNumber += str(tempHead.data)
        tempHead = tempHead.next
    tempHead = second
    while(tempHead):
        secondNumber += str(tempHead.data)
        tempHead = tempHead.next
    sum = str(int(firstNumber)+int(secondNumber))
    length = len(sum)
    i = 0
    newHead = None
    prev = Node(sum[i])
    i += 1
    newHead = prev
    while(i<length):
        temp = Node(sum[i])
        i += 1
        prev.next = temp
        prev = temp
    return newHead
        
