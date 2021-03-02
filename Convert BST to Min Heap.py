class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	


def getInorder(root,ans):
	if root is None:
		return
	getInorder(root.left,ans)
	ans.append(root.data)
	getInorder(root.right,ans)

def BSTtoHeap(root,ans):
	if root is None:
		return
	root.data = ans[0]
	ans.pop(0)
	BSTtoHeap(root.left,ans)
	BSTtoHeap(root.right,ans)


if __name__ == "__main__":
	root = Node(4)
	root.left = Node(2)
	root.right = Node(6)
	root.left.left = Node(1)
	root.left.right = Node(3)
	root.right.left = Node(5)
	root.right.right = Node(7)
	ans = []
	getInorder(root,ans)
	BSTtoHeap(root,ans)
