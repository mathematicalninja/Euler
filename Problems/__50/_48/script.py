# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#


def ModMult(a, b, M):
	A = a %M
	B = b %M
	return ((A *B) %M)
	pass


def run():
	Maxim = 1000
	Modr = 10**10
	Sum = 0
	for i in range(1, Maxim +1):
		Prod = 1
		for k in range(1, i +1):
			Prod = ModMult(Prod, i, Modr)
		pass
		Sum = (Sum + Prod) %Modr
	print(Sum, Prod)
	pass
