# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?


from functions.Integer import MakePrimes
from functions.Integer import isPrime
from functions.Integer import Obvs


def rotate(Integer):
	STR = str(Integer)
	Length = len(STR)

	for i in range(Length):
		yield int(STR[i:] +STR[:i])



def run():
	Maxim=1000000
	primes = MakePrimes(Maxim)
	Count = 3
	loop = 0
	for n in range(6, Maxim):
		loop = loop +1
		if loop %10000==0:
			print(loop)
		Succ = True
		if Obvs(n):
			continue
		for k in rotate(n):
			if not isPrime(k, primes)[0]:
				Succ=False
				break
		if Succ:
			Count = Count +1
			# print(n)
	print(Count)
	pass
