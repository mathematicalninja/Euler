def IsEven(inter):
	if inter %2==0:
		return True
	else:
		return False


def Divides(n, k):
	if n %k == 0:
		return True
	else:
		return False


def Product(Array):
	Prod = 1
	for n in Array:
		Prod = Prod *n
	return Prod


def HasFactor(n, factorList):
	for k in factorList:
		if n % k == 0:
			return True
	return False


def nCr(n, r):
	if n<=r:
		return 1
	else:
		top = 1
		bot = 1
		r = min(r, n -r)
		for i in range(n -r):
			top = top *(n -i)
			bot = bot *(n -r -i)
	return int(top /bot)


def MakePrimes(Maximum, primes=[2]):
	if Maximum<=2:
		return [2]

	from math import ceil

	def PrimeFactor(n, PrimesList):
		HalfWay = ceil(n**.5)
		for k in PrimesList:
			if k > HalfWay:
				return False
			if n % k == 0:
				return True
		return False

	for i in range(max(primes) +1, Maximum +1):
		if PrimeFactor(i, primes):
			continue
		else:
			primes.append(i)
	return primes
	pass


def DigitCount(Integer):
	return len(str(Integer))


def IsPalindrome(Integer):
	STR = str(Integer)
	for i in range(len(STR)):
		if STR[i] != STR[len(STR) -1 -i]:
			return False
	return True


def ModMult(a, b, M):
	A = a %M
	B = b %M
	return ((A *B) %M)
	pass


def Obvs(Integer, ind=0):
	STR=set(str(Integer)[ind:])
	if set.intersection(set(["2", "4", "5", "6", "8", "0"]), STR)!=set([]):
		return True


def Factorial(Integer):
	Result = 1
	for k in range(1, Integer +1):
		Result = Result * k
	return Result


def Triangular(Integer):
	return int(Integer *(Integer +1) /2)


def Pyramidal(Integer):
	return int(Integer *(Integer +1) *(2 *Integer +1) /6)


def Pentagonal(Integer):
	return int(Integer *(3 *Integer -1) /2)


def Hexagonal(Integer):
	return int(Integer *(2 *Integer -1))


def isSquare(Integer):
	return (abs(Integer)**.5 %1==0)


def isTriangular(Integer):
	return isSquare(8 *Integer +1)


def isPentagonal(Integer):
	if not isSquare(24 *Integer + 1):
		return False
	elif ((int((24 *Integer +1)**.5) +1) %6!=0):
		return False
	else:
		return True


def isHexagonal(Integer):
	if not isSquare(8 *Integer +1):
		return False
	elif (int((8 *Integer +1)**.5) +1) %4!=0:
		return False
	else:
		return True


def IsPythagorean(a, b, c):
	return a**2 +b**2 == c**2


def PySumTo(Integer):
	from math import floor
	a=1
	b=1
	c=Integer -2
	Triples = []
	Minimum = int(floor(Integer /3))
	while c > Minimum:
		if IsPythagorean(a, b, c):
			Triples.append([a, b, c])
		c = c -1
		b = b +1
		if b>=c:
			b=a +1
			a=a +1
			c=Integer -a -b
	return(Triples)


def FactorsOf(Integer):
	Factors = []
	Maximum = Integer**.5
	i = 1
	while True:
		if i > Maximum:
			break
		if Integer % i==0:
			Factors.append(i)
			if i != int(Integer / i):
				Factors.append(int(Integer / i))
		i = i +1
	return sorted(Factors)


def SmallestCommonFactor(a, b):
	def FactorsOf(Integer):
		Factors = []
		Maximum = Integer**.5
		i = 1
		while True:
			if i > Maximum:
				break
			if Integer % i==0:
				Factors.append(i)
				if i != int(Integer / i):
					Factors.append(int(Integer / i))
			i = i +1
		return sorted(Factors)

	Factors = FactorsOf(abs(min(a, b)))[1:]
	Max = abs(max(a, b))
	# ignore the fact that 1 divides a,b
	for k in Factors[1:]:
		if Max % k == 0:
			return k
	return False


def HighestCommonFactor(a, b):
	def FactorsOf(Integer):
		if Integer ==1:
			return [1]
		Factors = []
		Maximum = Integer**.5
		i = 1
		while True:
			if i > Maximum:
				break
			if Integer % i==0:
				Factors.append(i)
				if i != int(Integer / i):
					Factors.append(int(Integer / i))
			i = i +1
		return sorted(Factors)
	Factors = reversed(FactorsOf(abs(min(a, b))))
	Max = abs(max(a, b))
	# not excluding 1, as this is always a possible factor
	for k in Factors:
		if Max % k == 0:
			return k
	return False


def BiggestCoin(Value, Coins=[200, 100, 50, 20, 10, 5, 2, 1]):
	Head = Coins[0]
	Tail = Coins[1:]
	Sum = 0
	LoopCount = Value //Head
	if Tail !=[]:
		for t in range(0, LoopCount +1):
			Sum = Sum + BiggestCoin(Value - (t *Head), Tail)
		return Sum
	return int(Value % Head==0)


def PairSum(RowSum, MaxInd=False, Reversed=False):
	if not MaxInd:
		MaxInd = [RowSum +1, RowSum +1]
	for k in range(0, RowSum +1):
		y = RowSum -k
		x = k
		if (x >= MaxInd[0]) or (y >= MaxInd[1]):
			continue
		yield (y, x)



def PanCheck(n, q=9):
	STR = str(n)
	if len(STR)!=q:
		return False
	Digits = set(STR)
	if len(Digits)!=q:
		return False
	if Digits!=set([str(i) for i in range(1, q +1)]):
		return False
	else:
		return True


def IntReverse(Integer):
	from functions.Integer import IntReverse
	return intStrAdd(reversed(str(Integer)))
	pass


def intStrAdd(Array):
	STR = ""
	for n in Array:
		STR = STR +str(n)
	return int(STR)


def isPrime(n, primes=[2]):
	from functions.Integer import MakePrimes
	from functions.Integer import HasFactor
	from math import ceil

	if n<=1:
		return False, primes

	if n in primes:
		return True, primes
	elif n < max(primes):
		return False, primes
	elif HasFactor(n, primes):
		return False, primes
	else:
		primes = MakePrimes(ceil(n**.5), primes)
		if HasFactor(n, primes):
			return False, primes
		else:
			return True, primes


def CollatzSequence(Integer):
	def ColatzStep(Integer):
		if Integer % 2==0:
			return Integer /2
		else:
			return 3 * Integer +1
	Sequence = [Integer]
	while True:
		if Integer <=1:
			break
		else:
			Integer = ColatzStep(Integer)
			Sequence.append(int(Integer))
	return Sequence


def CheckedCollatzSequence(Integer, Checked={1: 1}):


	def ColatzStep(Integer):
		if Integer % 2 == 0:
			return int(Integer /2)
		else:
			return 3 * Integer +1


	def CollatzAddSeq(seq, Checked):
		CurrentValue = 1
		for n in reversed(seq):
			if n in Checked:
				if type(Checked[n]) is int:
					CurrentValue = Checked[n]
				else:
					Checked[n] = CurrentValue
			else:
				Checked[n] = CurrentValue
			CurrentValue = CurrentValue +1
		pass

	Sequence = [Integer]
	while True:
		if Integer <=1:
			break
		else:
			if Integer in Checked.keys():
				break
			else:
				Checked[Integer] = True
			Integer = ColatzStep(Integer)
			Sequence.append(int(Integer))
	CollatzAddSeq(seq=Sequence, Checked=Checked)
	return Checked


def GetAmicable(Integer):
	return sum(FactorsOf(Integer)) -Integer


def IsAmicable(Integer):
	Flip = sum(FactorsOf(Integer)) -Integer
	Flop = sum(FactorsOf(Flip)) -Flip
	return (Flop == Integer and Flip != Flop)


def IsPerfect(Integer):
	return (Integer == sum(FactorsOf(Integer)) -Integer)


def IsAbundant(Integer):
	return (sum(FactorsOf(Integer))>2 *Integer)


def IsDeficient(Integer):
	return (sum(FactorsOf(Integer))<2 *Integer)


def isNonRepeating(Integer):
	if(Integer %2!=0 and Integer %5!=0):
		return False
	else:
		k = Integer
		while True:
			if k %5==0:
				k = int(k /5)
			else:
				break
		while True:
			if k %2==0:
				k = int(k /2)
			else:
				break
		if k == 1:
			return True
		else:
			return False
	pass
