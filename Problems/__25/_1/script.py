# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def SumUnder(integer, factorList):
	if integer<2:
		return 0
	if factorList == []:
		return False
	if type(factorList) == int:
		factorList = [factorList]

	Dividables = []
	Sum = 0

	for i in range(2, integer):
		for k in factorList:
			if i %k ==0:
				if i not in Dividables:
					Dividables.append(i)

	for n in Dividables:
		Sum = Sum + n

	return Sum


if __name__ == "__main__":
	print(SumUnder(1000, [3, 5]))
