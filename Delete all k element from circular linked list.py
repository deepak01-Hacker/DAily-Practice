
#Deletion from a Circular Linked List


def deletionfromCLL(head,data,tail):
    tempHead = head
    prev = None
    while(tempHead.next!= head):
        if tempHead.data == data and prev == None:
            tail.next = head.next
            head = head.next
            tempHead = head
        elif tempHead.data == data:
            prev.next = tempHead.next
            tempHead = tempHead.next
        else:
            prev = tempHead
            tempHead = tempHead.next
    if prev != None and tempHead.data == data:
        prev.next = tempHead.next
    return head
            
