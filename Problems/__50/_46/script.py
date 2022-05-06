# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1 ^2
# 15 = 7 + 2×2 ^2
# 21 = 3 + 2×3 ^2
# 25 = 7 + 2×3 ^2
# 27 = 19 + 2×2 ^2
# 33 = 31 + 2×1 ^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#
from functions.Integer import isPrime
from functions.Integer import MakePrimes
from functions.Integer import IsEven


def run():
	DoubleLoop()
	pass


def DoubleSquare(Integer):
	from math import floor

	return BiggestSquare(floor(Integer /2))
	pass


def BiggestSquare(Integer):
	from math import floor
	return floor(Integer**.5)


def DoubleLoop():
	Maxim=10000
	primes = MakePrimes(Maxim)
	for Integer in range(2, Maxim):
		if IsEven(Integer):
			continue
		if isPrime(Integer)[0]:
			continue
		Bool, primes = CheckAll(Integer, primes)
		if Bool:
			print(Integer)
			break


def CheckAll(Integer, primes):
	Maxim = DoubleSquare(Integer)
	for i in range(1, Maxim +1):
		Bool, primes = isPrime(Integer -2 *i *i)
		if Bool:
			return False, primes
	return True, primes
