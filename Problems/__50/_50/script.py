# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from functions.Integer import MakePrimes


def run():
	Maxim = 1000000
	primes = MakePrimes(Maxim)
	print("Primes done.")

	print(NewLoop(primes, Maxim))
	pass


def NewLoop(primes, Maxim):
	Length = len(primes)
	print(Length)
	Longest = 1
	Biggest = 0
	for ind in range(Length -1):
		p = primes[ind]
		OldLong = Longest
		Sum = sum([primes[ind +j] for j in range(OldLong)])

		Cap=Length -ind -1 -OldLong
		if Cap < Longest:
			break
		for n in range(Cap):
			q=primes[ind +n +OldLong]
			Sum=Sum +q
			if Sum>Maxim:
				break
			elif Sum in primes:
				Longest=OldLong +n +1
				Biggest=Sum
			pass
	return(Biggest, Longest)

# 997651
