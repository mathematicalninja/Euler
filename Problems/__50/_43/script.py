# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
#
# d_2d_3d_4=406 is divisible by 2
# d_3d_4d_5=063 is divisible by 3
# d_4d_5d_6=635 is divisible by 5
# d_5d_6d_7=357 is divisible by 7
# d_6d_7d_8=572 is divisible by 11
# d_7d_8d_9=728 is divisible by 13
# d_8d_9d_10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from functions.Algebra import Permute
from functions.Integer import intStrAdd


def run():
	loop()
	pass


def loop():
	Maxim = 9
	Numbs = []
	for Perm in Permute([str(i) for i in range(0, Maxim +1)]):
		Numbs = Check(Perm, Numbs)

	# print(Numbs)
	print(sum(Numbs))
	pass


def Check(Perm, Numbs):
	if Perm[0]=="0":
		return Numbs
	Checkers = [
            [Perm[1], Perm[2], Perm[3]],
        				[Perm[2], Perm[3], Perm[4]],
        				[Perm[3], Perm[4], Perm[5]],
        				[Perm[4], Perm[5], Perm[6]],
        				[Perm[5], Perm[6], Perm[7]],
        				[Perm[6], Perm[7], Perm[8]],
        				[Perm[7], Perm[8], Perm[9]]
	]
	Primes = [2, 3, 5, 7, 11, 13, 17]
	for ind in range(7):
		if intStrAdd(Checkers[ind]) %Primes[ind]!=0:
			return Numbs
			break
	Numbs.append(intStrAdd(Perm))
	return Numbs

# 16695334890
