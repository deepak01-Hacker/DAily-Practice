def nearlySortedLL(head):
    stack = []
    heapq.heapify(stack)
    while(head!=None):
        heapq.heappush(stack,[head.data,head])
        head = head.next
    prevs = None
    head = None
    while(len(stack)):
        temp = heapq.heappop(stack)
        if prevs == None:
            head = temp[1]
            temp[1].prev = prevs
            prevs = temp[1]
        else:
            prevs.next = temp[1]
            temp[1].prev = prevs
            prevs = temp[1]
        temp[1].next = None
    return head
