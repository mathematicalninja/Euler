# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#


def run():

	Minum = 2
	Cap = 1000000
	Pow = 5
	Suc = []
	for n in range(Minum, Cap +1):
		Sum = 0
		for k in str(n):
			Sum = Sum +int(k)**Pow
		if Sum ==n:
			Suc.append(n)
	print(Suc)
	print(sum(Suc))
	pass
