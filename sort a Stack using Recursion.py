def sortedInsert(s,ele):

    if len(s) == 0 or ele > s[-1]:
        s.append(ele)
        return 
    else:
        temp = s.pop()
        sortedInsert(s,ele)
        s.append(temp)
    
def sortStack(s):
    if len(s) != 0:
        temp = s.pop()
        sortStack(s)
        sortedInsert(s,temp)

