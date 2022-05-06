# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

from functions.Integer import MakePrimes
from functions.Algebra import isPermute


def run():
	primes = MakePrimes(10000)
	print(len(primes))
	Checks = []
	for k in primes:
		if k>1000:
			Checks.append(k)
	Lenght = len(Checks)

	Checks = primes

	for i in range(Lenght):
		for j in range(i +1, Lenght):
			if isPermute(str(Checks[i]), str(Checks[j])):
				if (2 *Checks[j] -Checks[i]) in Checks:
					if isPermute(str(2 *Checks[j] -Checks[i]), str(Checks[i])):
						print(Checks[i], Checks[j], (2 *Checks[j] -Checks[i]))

	pass




# 2969 6299 9629
