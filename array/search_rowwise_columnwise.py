def solution(arr, n, target):
	i = 0
	j = n-1
	while i < n and j >= 0:
		cur = arr[i][j]
		if cur == target:
			return i, j
		elif cur > target:
			j -= 1
		elif cur < target:
			i += 1
	return -1


arr1 = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
print(solution(arr1, 4, 29))


