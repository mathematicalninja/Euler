# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?


def LazySum(a, b):
	return sum([int(d) for d in str(a**b)])


def run():
	Maxim = 100
	Biggest = 1
	for a in range(1, Maxim):
		for b in range(1, Maxim):
			Sm = LazySum(a, b)
			if Sm>Biggest:
				Biggest = Sm
	print(Biggest)
	pass
