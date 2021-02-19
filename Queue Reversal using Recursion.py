#User function Template for python3

def revUtil(q):
    if q.qsize():
        data = q.get()
        revUtil(q)
        q.put(data)

def rev(q):
    revUtil(q)
    return q

