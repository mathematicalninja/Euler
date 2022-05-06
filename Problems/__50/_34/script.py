# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from functions.Integer import Factorial


def run():
	Maxim = Factorial(9 +1)
	for k in range(3, Maxim):
		Sumim =0
		for d in str(k):
			Sumim = Sumim +Factorial(int(d))
		if Sumim ==k:
			print(k)
	pass
