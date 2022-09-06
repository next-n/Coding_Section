def swap_sum(x, y):
	x = x + y
	y = x - y
	x = x - y
	return x, y


def swap_multi(x, y):
	x = x * y
	y = x // y
	x = x // y
	return x, y


def swap_bitwise(x, y):
	x = x ^ y
	y = x ^ y
	x = x ^ y
	return x, y


print(swap_bitwise(1, 2))
