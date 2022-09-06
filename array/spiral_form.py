def solution(arr, rorc, porm, signcount, count, ilimit, jlimit, i, j):

	if rorc:
		if porm:
			for _ in range(jlimit):
				print(arr[i][j], end=" ")
				j += 1

			j -= 1
		else:
			for _ in range(jlimit):
				print(arr[i][j], end=" ")
				j -= 1

			j += 1
	else:
		if porm:
			for _ in range(ilimit):
				# print("i is", i, "j is", j)
				print(arr[i][j], end=" ")
				i += 1

			i -= 1
		else:
			for _ in range(ilimit):
				print(arr[i][j], end=" ")
				i -= 1

			i += 1
	# if rorc:
	# 	i += 1
	# else:
	# 	j += 1
	rorc = not rorc
	count += 1
	signcount += 1
	if count == 2:
		count = 0
		ilimit -= 1
		jlimit -= 1
	if signcount == 2:
		signcount = 0
		porm = not porm
	if porm:
		if rorc:
			j += 1
		else:
			i += 1
	else:
		if rorc:
			j -= 1
		else:
			i -= 1

	if ilimit or jlimit:
		solution(arr, rorc, porm, signcount, count, ilimit, jlimit, i, j)


def solution_sec(arr):
	fori, forj = [0, 1, 0, -1], [1, 0, -1, 0]
	n, m = len(arr), len(arr[0])
	i, j, di = 0, 0, 0
	seen = {}
	ans = []
	for _ in range(n * m):
		print(i, j)
		ans.append(arr[i][j])
		seen[(i, j)] = True
		newi, newj = i + fori[di], j + forj[di]
		if 0 <= newi < n and 0 <= newj < m and (newi, newj) not in seen:
			i = newi
			j = newj
		else:
			di = (di + 1) % 4
			i += fori[di]
			j += forj[di]
	return ans


arr1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
arr2 = [[5, 11, 30], [5, 19, 19]]

solution(arr2, True, True, 0, 1, len(arr2), len(arr2), 0, 0)
print("")
print(solution_sec(arr2))


