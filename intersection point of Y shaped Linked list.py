#User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

def intersetPoint(head1,head2):
    while(head1):
        if head1.data == 0:
            head1.data = 1001
        else:
            head1.data = -head1.data
        head1 = head1.next
    while(head2):
        if head2.data == 1001:
            return 0
        elif head2.data < 0:
            return -head2.data
        head2 = head2.next
    return -1

