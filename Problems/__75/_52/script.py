# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from functions.Algebra import isPermute


def run():
	Maxim= 150000
	Mult = 6
	for i in range(1, Maxim +1):
		Succ = True
		for m in range(2, Mult +1):
			# print(str(i), str(i *m))
			if not isPermute(str(i), str(i *m)):
				Succ = False
				break
		if Succ:
			print(i)
			return
	pass

# 142857
