# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is divisible by all of the numbers from 1 to 20?
#

from functions.Integer import Divides
from functions.Integer import MakePrimes




def DividesAll(Integer):
	primes = MakePrimes(Integer)
	PrimePowers = {}
	for p in primes:
		power = 1
		while True:
			if p**power <= Integer:
				power = power +1
			else:
				PrimePowers[p]=power -1
				break

	Product = 1

	for prime, power in PrimePowers.items():
		Product = Product * prime**power

	return Product


if __name__ == '__main__':
	print(DividesAll(20))
