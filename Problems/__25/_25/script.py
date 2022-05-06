# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def estimates():
	from decimal import Decimal, getcontext
	getcontext().prec = 60

	fiveish = Decimal(5**.5)
	phi = (1 +fiveish) /2
	psi = (1 -fiveish) /2
	Cap =10**1000
	n = 0
	while True:
		n = n +1
		if(((phi**n -psi**n) /fiveish)>Cap):
			print(n -1, (phi**(n -1) -psi**(n -1)) /fiveish)
			print(n, (phi**n -psi**n) /fiveish)
			break
	for n in range(1, 100 +1):
		if(((phi**n -psi**n) /fiveish)>Cap):
			print(n, (phi**n -psi**n) /fiveish)
			break
	for n in range(1, 10):
		print(n, (phi**n -psi**n) /fiveish)


def NextFib(a, b):
	return (b, a +b)


def run():
	a=1
	b=1
	bi=2
	Cap =10**1000
	while True:
		(a, b) = NextFib(a, b)
		bi=bi +1
		# if (bi>4780):
			# print(bi, )
		if len(str(b))==1000:
			print(bi)
			break

		if b>=Cap:
			# print(bi, b)
			break
	pass
