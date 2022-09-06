def solution(arr, target):
	m = {}
	t_count = 0
	for x in arr:
		if x in m:
			m[x] += 1
		else:
			m[x] = 1
	for x in arr:
		print(m)
		if target-x in m:
			t_count += m[target-x]
		if target-x == x:
			t_count -= 1
	return t_count // 2


arr1 = [1, 1, 1, 1]
print(solution(arr1, 2))

# print(arr1.index(1))