def convert_zigzag(arr):
	small = True
	for x in range(len(arr)-1):
		if small:
			if arr[x] > arr[x+1]:
				arr[x], arr[x+1] = arr[x+1], arr[x]
		else:
			if arr[x] < arr[x+1]:
				arr[x], arr[x+1] = arr[x+1], arr[x]
		small = not small
	return arr


arr1 = [4, 3, 7, 8, 6, 2, 1]
print(convert_zigzag(arr1))


