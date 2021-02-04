def findnormal(cap,capacity,n):
    for i in range(cap-1,-1,-1):
        if capacity[i][0] == n:
            capacity[i][1] += 1
    return

def findValue(cap,capacity):
    print(capacity)
    temp = [-1,-1]
    for i in range(cap):
        if capacity[i][1] > temp[0]:
            temp[0] = capacity[i][1]
            print(temp[0])
            temp[1] = i
    print(i)
    t = capacity.pop(temp[1])
    print(t)
    return t[0]

def pageFault(page,n,cap):
    ans =  0
    ans += cap
    temp = cap
    capacity = []
    checker = set()
    for i in range(cap):
        capacity.append([page[i],temp])
        checker.add(page[i])
        temp -= 1
    #print(capacity)
    for i in range(cap,n):
        if page[i] in checker:
            findnormal(cap,capacity,page[i])
        else:
            pagRemove = findValue(cap,capacity)
            print(pagRemove,checker)
            checker.remove(pagRemove)
            checker.add(page[i])
            capacity.append([page[i],1])
            ans += 1
    return ans
