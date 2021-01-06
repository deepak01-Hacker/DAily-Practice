
def partitionLast(st,en):
    if (st == en) or (st == None) or (en == None):
        return st
    curr = st
    pivot_prev = st
    pivot = en.data
    while(st!=en):
        if st == None:
            break
        if st.data < pivot:
            pivot_prev = curr
            temp = curr.data
            curr.data = st.data
            st.data = temp
            curr = curr.next
        st = st.next

    temp = curr.data
    curr.data = pivot
    en.data = temp

    return pivot_prev

def quickSort(start,end):
    if (start == end):
        return 
    pivot_prev = partitionLast(start,end)
    quickSort(start,pivot_prev)

    if (pivot_prev != None and pivot_prev == start):
        quickSort(pivot_prev.next,end)
    elif (pivot_prev != None and pivot_prev.next != None):
        quickSort(pivot_prev.next,end)
    

def last(head):
    while(head != None and head.next!=None):
        head = head.next
    return head
