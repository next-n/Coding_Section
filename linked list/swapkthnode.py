def swapkthnode(head, num, k):
	if k > num:
		return head
	left = k - 1
	right = num - left
	cur = head
	count = 0
	beforeleft = None
	leftmark = None
	rightmark = None
	beforeright = None
	while cur:
		if count == left - 1:
			beforeleft = cur
		if count == left:
			leftmark = cur
		count += 1
		if count == right:
			rightmark = cur
		if count == right - 1:
			beforeright = cur

		cur = cur.next
	if not beforeleft:
		leftnext = leftmark.next
		leftmark.next = None
		rightmark.next = leftnext
	else:
		leftnext = leftmark.next
		leftmark.next = None
		beforeleft.next = rightmark
		rightmark.next = leftnext
	beforeright.next = leftmark

	if beforeleft:
		return head
	else:
		return rightmark


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


r1 = Node(715)
r2 = Node(601)
r3 = Node(895)
r4 = Node(385)
r5 = Node(506)
r1.next, r2.next, r3.next, r4.next = r2, r3, r4, r5
print(swapkthnode(r1, 5, 2))