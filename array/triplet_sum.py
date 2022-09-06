def triplet(arr, target):
	arr.sort()
	for x in range(len(arr)-2):
		left = x + 1
		right = len(arr)-1
		while right > left:
			trisum = arr[x] + arr[left] + arr[right]
			if trisum == target:
				return True
			elif trisum < target:
				left += 1
			else:
				right -= 1
	return False


arr1 = [1, 2, 4, 3, 6]
target1 = 10
# print(triplet(arr1, target1))

# a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print(sum(a))
a = 1
b = []
b.append(a)
a = 20
print(b)