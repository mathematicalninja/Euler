# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from functions.Algebra import Permute


def run():
	Nines = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	Swaps = Permute(Nines)
	dic = {}
	Sum = 0
	SumB=0
	for Arrange in Swaps:
		a =ArrayStrSum(Arrange[:2])
		b =ArrayStrSum(Arrange[2:5])
		c =ArrayStrSum(Arrange[5:])
		if a *b ==c:
			print(a, b, c)
			dic[c]=True
		a =ArrayStrSum(Arrange[:1])
		b =ArrayStrSum(Arrange[1:5])
		c =ArrayStrSum(Arrange[5:])
		if a *b ==c:
			print(a, b, c)
			dic[c]=True
	for k in dic.keys():
		Sum = Sum +k
	print(Sum)




def ArrayStrSum(Array):
	Str = ""
	for i in Array:
		Str = Str +str(i)
	return int(Str)
