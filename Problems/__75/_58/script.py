# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

from functions.Integer import isPrime


#
# def TLdiag(Integer):
# 	if Integer == 0:
# 		return 0
# 	else:
# 		return ((2 *Integer)**2 +1)
# 	pass
#
#
# def TRdiag(Integer):
# 	if Integer == 0:
# 		return 0
# 	else:
# 		return ((2 *Integer)**2 -2* Integer +1)
# 	pass
#
#
# def BLdiag(Integer):
# 	if Integer == 0:
# 		return 0
# 	else:
# 		return ((2 *Integer +1)**2 -2 *Integer)
# 	pass

#
# def SquareDiag():
# 	def A():
# 		yield 0
# 		Value = 3
# 		Diff = 10
# 		while True:
# 			yield Value
# 			Value = Value + Diff
# 			Diff = Diff + 8
#
# 	def B():
# 		yield 0
# 		Value = 5
# 		Diff = 12
# 		while True:
# 			yield Value
# 			Value = Value + Diff
# 			Diff = Diff + 8
#
# 	def C():
# 		yield 0
# 		Value =7
# 		Diff = 14
# 		while True:
# 			yield Value
# 			Value = Value + Diff
# 			Diff = Diff + 8
#
# 	def D():
# 		yield 1
# 		Value = 9
# 		Diff = 16
# 		while True:
# 			yield Value
# 			Value = Value + Diff
# 			Diff = Diff + 8
#
# 	TR = A()
# 	TL = B()
# 	BL = C()
# 	BR = D()
# 	Diff = 8
# 	while True:
# 		yield (next(TR), next(TL), next(BL), next(BR))
# 	pass


def run():
	Maxim = 5000
	primes = [2]
	Square = SquareDiag()
	Count= 1
	Succs = 0
	while True:
		for i in range(Maxim):
			# print(int((Count -1) /4) +1, Count, Succs, Succs /Count)

			Tuple = next(Square)
			# print(int((Count -1) /2) +1, Tuple)
			for Diag in Tuple:
				Bool, primes = isPrime(Diag)
				# print(Diag, Bool)
				Succs = Succs + Bool
			Count = Count + 4
			if (Succs /Count <0.1)and Succs !=0:
				print(int((Count -1) /2) +1, Count, Succs, Succs /Count)
				yield
		yield Count, Succs
	pass


def oldLoop():
	primes = [2]
	Maxim = 2500
	primeCount = 0
	for i in range(1, Maxim +1):
		for Func in [TRdiag, TLdiag, BLdiag]:
			Bool, primes = isPrime(Func(i))
			# print(Func(i), Bool)
			primeCount = primeCount +Bool
		# print(4 *i +1, primeCount, primeCount /(4 *i +1))
		if primeCount /(4 *i +1)<0.1:
			print(2 *i +1)
			break
	print(primeCount /(4 *Maxim +1))
		# print(TRdiag(i))
		# print(TLdiag(i))
		# print(BLdiag(i))
	pass




def SquareDiag():
	yield [1]
	yield (3, 5, 7, 9)
	Q = 9
	Edge = 2
	while True:
		Edge = Edge + 2
		F = Q + 4* Edge
		yield Q +Edge, Q +2 *Edge, Q +3 *Edge, F
		Q = F
