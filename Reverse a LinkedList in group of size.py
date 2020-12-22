class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def makeLL(LL):
    head = Node(LL[0])
    temp = head
    for i in range(1,len(LL)):
        temp.next = Node(LL[i])
        temp = temp.next
    return head

def reverse(head,k):
    group = 0
    prev = None
    curr = head
    H = None
    temp1 = head
    temp2 = None
    while(curr!=None):
        if group%k == 0:
            if group//k == 1 and H is None:
                H = prev
            if (group//k) >= 2:
                temp1.next = prev
                prev = None
            temp1 = temp2
            temp2 = curr
        nexts = curr.next
        curr.next = prev
        prev = curr
        curr = nexts
        group += 1
    if temp1 != None:
        temp1.next = prev
        head = prev
        t = 0
        temp2.next= None
    else:
        H = prev
    curr = H
    t = 0
    while(curr and t != 10):
        t+= 1
        print(curr.data,end=" ")
        curr = curr.next
    print()



if __name__ == "__main__":
    LL = [1,2,3,4,5,6,7,8]
    k = 7
    H = makeLL(LL)
    reverse(H,k)
