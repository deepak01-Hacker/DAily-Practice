#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def segregate(head):
    tempHead = head
    zeros = 0
    ones = 0
    while(tempHead):
        if tempHead.data == 0:
            zeros += 1
        elif tempHead.data == 1:
            ones += 1
        tempHead = tempHead.next
    tempHead = head
    while(tempHead):
        if zeros > 0:
            tempHead.data = 0
            zeros -= 1
        elif ones>0:
            tempHead.data = 1
            ones -= 1
        else:
            tempHead.data = 2
        tempHead = tempHead.next
    return head
