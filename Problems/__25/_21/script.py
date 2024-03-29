# Let d(n) be defined as the sum of proper divisors of n(numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142
# so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from functions.Integer import FactorsOf


def GetAmicable(Integer):
	# print(Integer, FactorsOf(Integer))
	return sum(FactorsOf(Integer)) -Integer


def IsAmicable(Integer):
	Flip = sum(FactorsOf(Integer)) -Integer
	Flop = sum(FactorsOf(Flip)) -Flip
	return (Flop == Integer and Flip != Flop)


def AmicableSum(Maximum):
	Sum =0
	# for n in range(1, Maximum +1):
	# 	Amicables[n] = GetAmicable(n)
	# 	# print(Amicables[n])
	for n in range(1, Maximum +1):
		if IsAmicable(n):
			print(n)
			Sum = Sum +n
	# print(Amicables)
	return Sum


def run():
	print(AmicableSum(10000))
	pass
