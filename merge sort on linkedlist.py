def merge(left,right):
    result = None
    if left is None:
        return right
    if right is None:
        return left
    if left.data <= right.data:
        result = left
        left.next = merge(left.next,right)
    else:
        result = right
        right.next = merge(left,right.next)
    return result

def mid(head):
    slow = head
    fast = slow
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeSort(head):
    if head == None or head.next == None:
        return head
    
    middle = mid(head)
    nextMiddle = middle.next
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(nextMiddle)

    sortedLL = merge(left,right)
    return sortedLL

def printLL(head):
    tempHead = head
    while(tempHead):
        print(tempHead.data,end=" ")
        tempHead = tempHead.next
    print()
