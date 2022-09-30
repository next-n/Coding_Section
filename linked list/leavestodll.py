def convertToDLL(t):
	def conver(root, dll):
		if not root:
			return dll, None
		if not root.left and not root.right:
			root.left = dll
			dll.right = root
			dll = root
			return dll, None
		ld, root.left = conver(root.left, dll)
		rd, root.right = conver(root.right, ld)

		return rd, root

	ans = Node(0)
	pointer1 = ans
	conver(t, pointer1)
	return ans.right


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def printlink(a):
	arr = []
	while a:
		arr.append(a.data)
		a = a.right
	return arr


def inorder(a):
	if not a:
		return
	inorder(a.left)
	print(a.data)
	inorder(a.right)


r1 = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
r1.left, r1.right = r2, r3
r2.left = r4
print(printlink(convertToDLL(r1)))
print(r1.right.data)


