def sortbit(array):
	def merge(a, b):
		i, j = 0, 0
		n = len(a)
		m = len(b)
		ans = []
		while i < n and j < m:
			ac = bin(a[i])[2::].count('1')
			bc = bin(b[j])[2::].count('1')
			if ac < bc:
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
		if len(arr) == 1:
			return arr
		start = 0
		end = len(arr) - 1
		mid = (start + end) // 2
		left = divide(arr[start:mid + 1])
		right = divide(arr[mid + 1:end + 1])
		return merge(left, right)

	return divide(array)


def sortbit_inplace(array):
	# print("ori", array)
	def merge(arr, start, end, mid):
		s1 = start
		s2 = mid + 1

		while s1 <= mid and s2 <= end:
			s1c = arr[s1][1]
			s2c = arr[s2][1]
			if s2c > s1c:
				arr.insert(s1, arr.pop(s2))
				mid += 1
				s2 += 1
			else:
				pass
			s1 += 1

	def divide(arr, l, r):
		if r > l:
			m = l + (r - l) // 2
			divide(arr, l, m)
			divide(arr, m + 1, r)
			merge(arr, l, r, m)
			# print("a", arr)

	arr1x = [[x, bin(x)[2::].count('1')] for x in array]
	divide(arr1x, 0, len(array) - 1)
	temp = [x[0] for x in arr1x]
	array.clear()
	for x in temp:
		array.append(x)


arr1 = [5, 2, 3, 9, 4, 6, 7, 15, 32]
print(sortbit(arr1))
sortbit_inplace(arr1)
print(arr1)