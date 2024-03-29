# Pentagonal numbers are generated by the formula, P_n=n(3n−1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, P_j and P_k, for which their sum and difference are pentagonal and D = |P_k − P_j| is minimised; what is the value of D?

from functions.Integer import Pentagonal


def run():
	Maxim = 2200
	Pents = []
	for i in range(1, 2 *Maxim):
		Pents.append(Pentagonal(i))
	pass

	Successes = []
	for i in range(Maxim -1):
		for j in range(i +1, Maxim):
			if Pents[j] -Pents[i] not in Pents:
				continue
			if Pents[j] +Pents[i] not in Pents:
				continue
			print(Pents[i] -Pents[j])
