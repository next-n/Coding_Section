def lns(ns):
	count = 1
	i = 1
	n = len(ns)
	temp = ""
	while i < n:
		if ns[i] == ns[i-1]:
			count += 1
		else:
			temp += str(count)+str(ns[i-1])
			count = 1
		i += 1
	temp += str(count)+str(ns[n-1])
	return temp


def lookandsay(n):
	if n == 1:
		return "1"
	start = "1"
	for x in range(n-1):
		start = lns(start)
	return start


print(lookandsay(4))
