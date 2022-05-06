# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
# For example,
#
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?


def DigitSquare(Integer):
	return sum([int(d)**2 for d in str(Integer)])


def run():
	Maxim = 10**7
	Values = {1: 1, 89: 89}
	Count = 0
	for k in range(1, Maxim):
		Current = k
		Seq = []
		while True:
			Seq.append(k)
			Current = DigitSquare(Current)
			if Current in Values:
				Res = Values[Current]
				for j in Seq:
					Values[j] = Res
				break
				pass
			pass
		pass
	for t, Res in Values.items():
		if Res ==89:
			if t<Maxim:
				Count = Count + 1
	print(Count)
	pass
