def s(arr):
	max_so_far = 0
	m = {}
	temp = 0
	for x in arr:
		if x not in m:
			temp += 1
			m[x] = 1
		else:
			m.clear()
			max_so_far = max(max_so_far, temp)
			temp = 0
	return max_so_far


arr1 = "ABDEFGABEF"
arr2 = "BBBB"
arr3 = "GEEKSFORGEEKS"
print(s(arr1))
print(s(arr2))
print(s(arr3))
