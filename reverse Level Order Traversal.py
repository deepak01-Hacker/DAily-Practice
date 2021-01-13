#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    ans = []
    queue =  []
    queue.append(root)
    while(True):
        len_ = len(queue)
        if len_:
            t = []
            while(len_):
                curr = queue.pop(0)
                t.append(0,curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                len_ -= 1
            ans.insert(0,t)
        else:
            break
    return ans
