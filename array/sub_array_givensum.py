def solution(arr, s):
	n = len(arr)
	k = 0
	temp = 0
	for _ in range(n):
		temp += arr[_]
		while temp > s and k != _:
			temp -= arr[k]
			k += 1
		if temp == s:
			return k+1, _+1
	return [-1]


arr1 = [1, 2, 3, 7, 5]
print(solution(arr1, 12))
