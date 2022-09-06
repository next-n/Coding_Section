def sms(s, p):

	m_o = {}
	for x in p:
		if x in m_o:
			m_o[x] += 1
		else:
			m_o[x] = 1
	count = len(p)
	i = 0
	n = len(s)
	start = []
	end = 0
	m = m_o.copy()
	print(m)
	while i < n:
		if s[i] in m and m[s[i]] > 0:
			start.append(i)
			count -= 1
			m[s[i]] -= 1

		elif s[i] in m and m[s[i]] == 0:
			print("third if", s[i], m)
			start.append(i)
			start.pop(0)
			i = start[0]
			m = m_o.copy()
			print("after t if", m, "i", i)
			count = len(p)
			continue
		if count == 0:
			end = i + 1
			return s[start[0]:end]
		i += 1
	return -1


s1 = "timetopractice"
p1 = "toc"
print(sms(s1, p1))
a = "a"
print(ord("a")- ord(a))