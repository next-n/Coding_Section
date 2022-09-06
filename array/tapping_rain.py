def solution(arr):
	left, right = [], []
	left_max, right_max, last, ans = 0, 0, len(arr) - 1, 0

	for x in range(len(arr)):
		left_max = max(arr[x], left_max)
		left.append(left_max)
		right_max = max(arr[last-x], right_max)
		right.append(right_max)
	# print(left, right)
	for x in range(len(arr)):
		ans += (min(left[x], right[x]) - arr[x])
	return ans


arr1 = [3, 0, 2, 0, 4]
print(solution(arr1))
