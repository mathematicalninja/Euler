# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


from math import ceil


def PrimeFactor(n, PrimesList):
	HalfWay = ceil(n**.5)
	for k in PrimesList:
		if k > HalfWay:
			return False
		if n % k == 0:
			return True
	return False


def ManyPrimes(Length):
	primes = [2]
	Current = 3
	for i in range(Length -1):
		while True:
			if not PrimeFactor(Current, primes):
				primes.append(Current)
				Current = Current + 2
				break
			else:
				Current = Current + 2
	return primes
	pass


if __name__ == '__main__':
	Primelings = ManyPrimes(10001)
	print(Primelings[-1])
