# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from functions.Integer import isPrime
from functions.Algebra import Permute
from functions.Integer import intStrAdd



def run():
	# 1+2,4+5,7+8 are all divisable by 3, so Maxim < 8
	Maxim = 7
	print("Primes are done")
	primes = [2]
	for n in range(1, Maxim +1):
		for perm in Permute([i for i in range(1, n +1)]):
			Integer = intStrAdd(perm)
			Bool, primes = isPrime(Integer, primes)
			if Bool:
				print(type(Integer))
				print(Integer)
	pass
# 7652413
