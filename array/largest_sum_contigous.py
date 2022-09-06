def solution(arr):
	max_so_far = float("-inf")
	max_end = 0
	for x in arr:
		max_end += x
		if max_so_far < max_end:
			max_so_far = max_end
		if max_end < 0:
			max_end = 0
	return max_so_far


def solution_dynamic(arr):
	cur_max = arr[0]
	max_so_far = arr[0]
	for x in range(1, len(arr)):
		cur_max = max(arr[x], cur_max+arr[x])
		max_so_far = max(cur_max, max_so_far)
	return max_so_far


arr1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(solution(arr1))
print(solution_dynamic(arr1))
