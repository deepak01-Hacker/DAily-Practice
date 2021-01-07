#Hint : Two pointer Technique 


def findpairsum(head,tail,data):
    i = head
    j = tail
    while(i!=j) and (i.data <= j.data):
        pairSum = i.data + j.data
        if pairSum == data:
            print(j.data,i.data)
            i = i.next
            j = j.prev
        elif pairSum < data:
            i = i.next
        else:
            j = j.prev
    
