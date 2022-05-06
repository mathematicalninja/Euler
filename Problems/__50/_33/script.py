# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from functions.Integer import intStrAdd
from functions.Integer import HighestCommonFactor


def run():
	fracs = []
	for a in range(1, 9 +1):
		for b in range(a, 9 +1):
			for c in range(1, 9 +1):
				if b +c<=1:
					continue
				else:
					tops=[intStrAdd([a, c]), intStrAdd([c, a])]
					bots=[intStrAdd([b, c]), intStrAdd([c, b])]
					for Top in tops:
						for Bot in bots:
							if Top /Bot ==a /b:
								if a!=b:
									print(Top, "/", Bot)
									fracs.append([a, b])
	print(fracs)
	A=1
	B=1
	for pair in fracs:
		A=A *pair[0]
		B=B *pair[1]
	Fac = HighestCommonFactor(A, B)
	print(int(B /Fac))
	# Prod = Prod *B /Fac
