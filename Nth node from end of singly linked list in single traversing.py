#User function Template for python3
'''
	Your task is to return the data stored in
	the nth node from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def getNthFromLast(head,n):
    slow = head
    fast = head
    data = -1
    len = 0
    while(fast):
        len += 1
        if len >= n:
            data = slow.data
            slow = slow.next
        fast = fast.next
    return data
            
    
