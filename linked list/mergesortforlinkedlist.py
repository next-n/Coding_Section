def mergeSort(head):
	def merge(a, b):
		result = None
		pointer = None
		while a and b:
			if a.data < b.data:
				if not result:
					result = a
					pointer = result
				else:
					pointer.next = a
					pointer = pointer.next
				a = a.next
			else:
				if not result:
					result = b
					pointer = result
				else:
					pointer.next = b
					pointer = pointer.next
				b = b.next
		if a:
			pointer.next = a
		if b:
			pointer.next = b
		return result

	def divide(root):
		if not root.next:
			return root
		slow = root
		fast = root
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		rislow = slow.next
		slow.next = None
		left = divide(root)
		right = divide(rislow)
		return merge(left, right)

	return divide(head)


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


r1 = Node(3)
r2 = Node(5)
r3 = Node(2)
r4 = Node(4)
r5 = Node(1)
r1.next, r2.next, r3.next, r4.next = r2, r3, r4, r5
print(mergeSort(r1).data)