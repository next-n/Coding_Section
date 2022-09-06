def duplicate(arr):
	ans = []
	m = {}
	for x in arr:
		if x in m:
			if m[x] == 1:
				ans.append(x)
			m[x] += 1
		else:
			m[x] = 1
	if ans:
		ans.sort()
		return ans
	else:
		return -1


arr1 = [2, 3, 1, 2, 3]
print(duplicate(arr1))
