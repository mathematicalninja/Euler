# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.


def run():
	CurrentLeft =[0, 1]
	Maxim = 10**6
	Goal = 3 /7
	Num = 0
	Den = 1
	while True:
		if Den > Maxim:
			print(CurrentLeft)
			return CurrentLeft
		else:
			Current = CurrentLeft[0] /CurrentLeft[1]
			if Current < Num / Den:
				if Num /Den < Goal:
					CurrentLeft = [Num, Den]
			if Goal > Num / Den:
				Num += 1
			if Goal <= Num / Den:
				Den += 1
		# print(Num, Den)
		# print(CurrentLeft)
	pass

# 428570 / 999997
