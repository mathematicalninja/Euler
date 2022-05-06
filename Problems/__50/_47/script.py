# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from functions.Integer import MakePrimes
from functions.Integer import isPrime


def run():
	Maxim =150000
	n=4
	print(nPrimes(n, Maxim))


def nPrimes(n, Maxim):
	primes = MakePrimes(1000)
	for k in range(2, Maxim +1):
		if len(PrimeFactorsOf(k, primes))>= n:
			for j in range(1, n):
				if len(PrimeFactorsOf(k +j, primes))>= n:
					if j ==n -1:
						return k
					continue
				else:
					Succ=False
					break
			if Succ:
				return k
		else:
			continue
	return "Need a bigger Maxim"
	pass


def PrimeFactorsOf(Integer, primes=[2]):

	Bool, primes = isPrime(Integer, primes)
	if Bool:
		return [Integer]

	Factors = []
	for p in primes:
		if Integer %p==0:
			Factors.append(p)
	return sorted(Factors)
