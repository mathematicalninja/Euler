# φ(n)  = n*prod_[p|n](1-1/p)

# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

from functions.Integer import MakePrimes
from functions.Integer import FactorsOf


def HighestPowerFactor(n, p):
	if n %p !=0:
		return False
	else:
		Count = 0
		while True:
			if n % p ==0:
				Count +=1
				n = int(n / p)
			else:
				return Count
			if n <=1:
				return Count
	pass


def φ(n, primes):

	# this is not Euler Totient function, it is n/φ(n)
	# plus a while bunch of shortcuts
	factors = FactorsOf(n)

	Fac = []
	for k in factors:
		if k in primes:
			Fac.append(k)

	Powers = {}
	for p in Fac:
		Powers[p]=HighestPowerFactor(n, p)

	if Powers == {}:
		return -1

	Top = 1
	for p, Pow in Powers.items():
		Top = Top *p /(p -1)
	return Top


def run():
	Maxim = 10**6
	Minum = 1
	primes = MakePrimes(Maximum=int(Maxim**(1 /3)), primes=[2])
	print("primes done")
	highest = [0, 0]
	for n in range(Minum, Maxim +1):
		if n %10000 ==0:
			print(n)
		Val = φ(n, primes)
		if Val >highest[1]:
			highest = [n, Val]

	print(highest)
	pass

# 510510
