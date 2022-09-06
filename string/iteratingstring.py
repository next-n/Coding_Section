def itr(s):
	def sa(s_):
		lps = [0]
		le = 0
		i = 1
		m = len(s_)
		while i < m:
			if s_[i] == s[le]:
				le += 1
				i += 1
				lps.append(le)
			else:
				if le == 0:
					lps.append(0)
					i += 1
				else:
					le = lps[le-1]
		if lps:
			print(lps)
			return lps.pop()
		else:

			return 0
	div = sa(s)
	n = len(s)
	print(div, n-div, n)
	if div == 0:
		return False
	elif n % (n-div) != 0:
		return False
	else:
		return True
	# print(temp, div)
	# for x in range(div+div, len(s)+1, div):
	# 	temp_s = s[div: x]
	# 	div = x
	# 	if temp_s != temp:
	# 		return False

	# return True


s1 = "abadabad"
s2 = "ababab"
print(itr(s2))
