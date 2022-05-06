# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def SumPrimes(Maximum):
	from functions.Integer import MakePrimes

	Primes = MakePrimes(Maximum)

	Sum = 0

	for p in Primes:
		Sum = Sum +p

	return Sum


def run():

	print(SumPrimes(2000000))
