# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.
#
# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.

# First thing to note is that if p^2|n, then p|(p+n/p), so this is not prime, unless n =p^2
# But if n = p^2, 2|(p+n/p) = 2|(2p)

# so only need to check numbers that are composed of multiple unique primes


from functions.Integer import MakePrimes


def run():
	Maxim = 10**4
	primes = MakePrimes(Maxim)
	print(primes)
	Count = 0
	for n in range(2, Maxim +1):
		if n in primes:
			continue
		if n %4 ==0:
			continue
		if n %9 ==0:
			continue
		if n %16 ==0:
			continue
		if n % 25 ==0:
			continue
		Fail = False
		for p in primes[3:int(n**.5) +1]:
			if n % p**2==0:
				Fail = True
				break
		if Fail:
			continue
		else:
			Facts = UniquePrimeFactors(n, primes)
			if len(Facts) ==2 and 2 not in Facts:
				continue
			elif len(Facts) ==2 and (Facts[0] +Facts[1] not in primes):
				continue
			else:
				pass
				Count +=1
	pass
	print(Count)


def UniquePrimeFactors(n, primes):
	# only works if n has no square factors
	Out = []
	for k in primes:
		if n %k==0:
			Out.append(k)
			n = int(n / k)
			if n == 1:
				return Out
