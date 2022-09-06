def solution(arr, k):
	i = 0
	min_so_far = float("inf")
	temp, count, ans = 0, 0, 0
	for x in range(len(arr)):
		temp += arr[x]
		if x >= k-1:
			count += 1
			if temp < min_so_far:
				min_so_far = temp
				ans = count
			temp -= arr[i]
			i += 1
	return ans


arr1 = [30, 20, 10]
k1 = 1
print(solution(arr1, k1))
