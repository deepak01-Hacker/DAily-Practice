#User function Template for python3
'''
	Your task is to remove duplicates from given 
	unsorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: head of the list after removing the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def removeDuplicates(head):
    checker = set()
    temp = head
    while(temp and temp.next):
        checker.add(temp.data)
        if temp.next.data in checker:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
        

