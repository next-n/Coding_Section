def ps(s, ans, temp, indx, n, m):
	if indx == n:
		a = "".join(temp)
		ans.append(a)
		return
	for x in range(n):
		if m[x] == 1:
			continue
		else:
			temp.append(s[x])
			m[x] = 1
			ps(s, ans, temp, indx+1, n, m)
			temp.pop()
			m[x] = 0
	return ans


def _2(s, i, k, ans):
	if k == 0:
		ans.append("".join(s))
		return
	for x in range(k):
		s[i], s[i+x] = s[i+x], s[i]
		_2(s, i+1, k-1, ans)
		s[i], s[i+x] = s[i+x], s[i]
	return ans


s1 = "abc"
m1 = [0 for x in s1]
print(ps(s1, [], [], 0, len(s1), m1))
print(_2(list(s1), 0, len(s1), []))
