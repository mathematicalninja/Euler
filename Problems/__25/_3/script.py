# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def LargestFactor(Integer):
	from functions.Integer import HasFactor
	from functions.Integer import MakePrimes
	from math import floor

	primes = MakePrimes(floor(Integer**(.5)))
	Highest = 1

	if Integer<=1:
		return 0

	for p in reversed(primes):
		if Integer % p == 0:
			return p
	else:
		return None



if __name__=="__main__":
	print(LargestFactor(600851475143))
