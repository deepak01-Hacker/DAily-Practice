def printSubSeqRec(st,n,index,curr):
    if index == n:
        return 
    if curr :
        print(*curr)
    for i in range(index+1,n):
        curr.append(st[i])
        printSubSeqRec(st,n,i,curr)
        curr.pop()
    return

def printSubSeqRec1(st,n):
    printSubSeqRec(st,n,-1,[])

if __name__ == "__main__":
    st = "ABCD"
    printSubSeqRec1(st,len(st))
