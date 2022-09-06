def sec_largest(arr):
	maxx = float("-inf")
	sec = float("-inf")
	for x in arr:
		if x == maxx:
			continue
		elif x > maxx:
			sec = maxx
			maxx = x
		elif x > sec:
			sec = x
	if sec != float("-inf"):
		return sec
	else:
		return -1


arr1 = [10, 10, 1, 1, 2]
print(sec_largest(arr1))
