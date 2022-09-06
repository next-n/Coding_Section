def anam(a, b):
	x = str(min(a, b, key=len))
	y = str(max(a, b, key=len))
	m = {}
	# m2 = {}
	for i in x:
		if i in m:
			m[i] += 1
		else:
			m[i] = 1
	newtemp = ""
	for i in y:
		if i in m:
			if m[i] > 0:
				newtemp += i

				m[i] -= 1

	if sorted(x) == sorted(newtemp):
		return len(y) - len(newtemp)
	else:
		return 0


str1 = "bca"
str2 = "acb"
# print(max(str1, str2, key=len))
print(anam(str1, str2))
a1 = "idifhdsihvdishfidhd"
a2 = "a"
# print(min(a1, a2, key=len))

