def findmiddle(root):
	slow = root
	fast = root
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
	return slow


class node:
	def __init__(self, data):
		self.data = data
		self.next = None


def merge(a, b):
	i, j = 0, 0
	n = len(a)
	m = len(b)
	ans = []
	while i < n and j < m:
		ab = int(str(a[i]) + str(b[j]))
		ba = int(str(b[j]) + str(a[i]))
		if ba > ab:
			ans.append(b[j])
			j += 1
		else:
			ans.append(a[i])
			i += 1
	while i < n:
		ans.append(a[i])
		i += 1
	while j < m:
		ans.append(b[j])
		j += 1
	return ans


def divide(arr):
	if not arr:
		return
	if len(arr) == 1:
		return arr
	left = 0
	right = len(arr)-1
	mid = (left+right) // 2
	left = divide(arr[left:mid+1])
	right = divide(arr[mid+1:right+1])
	return merge(left, right)


arr1 = [3, 30, 34, 5, 9]
print(divide(arr1))