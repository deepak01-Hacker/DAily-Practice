#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''

def length(head):
    tempHead = head
    len = 0
    while(tempHead):
        len += 1
        tempHead = tempHead.next
    return len

def isPalindrome(head):
    l = length(head)
    curr = head
    prev = None
    index = 0
    while(curr != None):
        if l//2 <= index:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        else:
            curr = curr.next
        index += 1
    newHEad = prev
    while(head and newHEad):
        if head.data != newHEad.data:
            return False
        head = head.next
        newHEad = newHEad.next
    return True
            
