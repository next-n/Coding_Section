import math


def solution(arr, d):
	n = len(arr)
	d = d % n
	g_c_d = math.gcd(n, d)
	for i in range(g_c_d):
		temp = arr[i]
		j = i
		while True:
			k = j + d
			if k >= n:
				k -= n
			if k == i:
				break
			arr[j] = arr[k]
			j = k
		arr[j] = temp
	return arr


arr1 = [0, 1, 2, 3]
print(solution(arr1, 1))

