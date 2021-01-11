
#Solution in O(n) and O(1) space 


def modifyLinkedListEvenOdd(head):
    tail = None
    tempHead = head
    main_tail = None
    while(tempHead.next):
        if tempHead.data%2 == 0:
            main_tail = tempHead
        tempHead = tempHead.next
    tail = tempHead
    print(tail.data)
    tempHead = head
    prev = None
    temp = Node(0)
    tailHelper = temp
    while(tempHead):
        if tempHead.data%2 != 0:
            nexts = tempHead.next
            if prev != None:
                prev.next = tempHead.next
            else:
                head = head.next
            temp.next = tempHead
            tempHead.next = None
            temp = temp.next
            tempHead = nexts
        else:
            prev = tempHead
            tempHead = tempHead.next
    main_tail.next = tailHelper.next
    return head
