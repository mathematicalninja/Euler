# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d_n represents the nth digit of the fractional part, find the value of the following expression.
#
# d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

from functions.Integer import Product


def run():
	Maxim = 1000000
	maxPow= 6
	# Pow = 1
	Sumim = 0
	Ints=[]
	Digs = []
	for Pow in range(1, maxPow +1):
		Goal = 10**(Pow) -1
		Aim = (Goal -Sumim) //Pow
		Rem = (Goal -Sumim) % Pow
		print(Goal -Sumim)
		print(Aim)
		print(Rem)
		Ints.append(10**(Pow -1) +Aim)
		Digs.append(str(Ints[-1])[Rem])
		Sumim=Sumim+ 9 *10**(Pow -1) *Pow
		print(Sumim)
	pass
	print(Ints)
	print(Digs)
	Prod = 1
	for d in Digs:
		Prod = Prod *int(d)
	print(Prod)
	AltStr(maxPow)


def AltStr(MaxPow):
	STR=""
	for i in range(1, 10**MaxPow):
		STR = STR +str(i)
	print([STR[10**k -1] for k in range(1, MaxPow)])
	print(Product([int(STR[10**k -1]) for k in range(1, MaxPow)]))
