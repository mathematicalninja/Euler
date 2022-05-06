# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from functions.Integer import isPrime
from functions.Integer import MakePrimes
from functions.Integer import Obvs


def run():
	Maxim = 100000
	Count = 0
	Sum = 0
	primes = MakePrimes(Maxim)
	for n in range(10, Maxim +1):
		if Obvs(n, 1):
			continue
		STR = str(n)
		Succ = True
		for i in range(1, len(STR)):
			if not isPrime(int(STR[:i]))[0]:
				Succ = False
				break
			if not isPrime(int(STR[i:]))[0]:
				Succ = False
				break
		if not Succ:
			continue
		if not isPrime(n)[0]:
			continue
		if Succ:
			Count = Count +1
			Sum = Sum +n
			print(n)
			pass
	print(Count)
	print(Sum)

	# 8920+739397
	# 748317
	pass
