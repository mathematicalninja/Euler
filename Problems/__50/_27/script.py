# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

# from functions.Integer import ShrunkFactorsOf
from functions.Integer import SmallestCommonFactor
from functions.Integer import MakePrimes
from functions.Integer import HasFactor
from functions.Integer import isPrime



def polyEval(Quad, n):
	# Quad = [a,b]
	# for n^2 + an + b
	return n *n +n *Quad[0] +Quad[1]




def PrimeSequence(Quad, primes, check=False):
	# Quad = [a,b]
	# for n^2 + an + b
	n= 0
	while True:
		QuadVal = polyEval(Quad, n)
		Bool, primes = isPrime(QuadVal, primes)
		if check:
			print(QuadVal, Bool)
		# print(QuadVal, Bool)

		if Bool:
			n = n +1
			continue
		else:
			# print(n)
			return n, primes
	pass




primes = MakePrimes(1000)


def run():
	Count = 0
	polys = []
	global primes
	SmallPrimes = primes[0:13]
	Size = 1000
	minum = 40
	# |a|<1000 strict, |b|<=1000 weak
	for a in range(1, Size):
		for b in range(1, Size +1):
			Count = Count +1
			scf = SmallestCommonFactor(a, b)
			if a==1 and b==41:
				print("this one here", scf)
			if scf is False or scf >=minum:
				for sig in signs:
					n, primes = PrimeSequence(Quad=[a *sig[0], b *sig[1]], primes=primes)
					if n>=minum:
						minum = n
						polys.append([a *sig[0], b *sig[1]])
			# else:
			# 	n, primes = PrimeSequence(Quad=[a, b], primes=primes)
			# 	if n>=minum:
			# 		minum = n
			# 		polys.append([a, b])
			if Count %25000==0:
				print(Count)
	print(polys)
	pass
	print(PrimeSequence([1, 41], primes))


signs=[
    [1, -1],
    [-1, 1],
    [1, 1],
    [-1, -1]
]
