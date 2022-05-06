# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5Z|
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from functions.Integer import isNonRepeating


def RecurringDigits(Integer):
	if Integer<=1:
		return False
	else:
		Digits= {}
		Remainder = 1
		place=0
		while True:
			place = place +1
			(d, r)=(10 *Remainder //Integer, 10 *Remainder %Integer)
			if (d, r) in Digits.keys():
				Difference =place -Digits[(d, r)]
				return Difference, Digits
			else:
				Digits[(d, r)] = place
				Remainder = r


def run():
	Maxim = 0
	Num = 0
	for i in range(2, 1000 +1):
		if isNonRepeating(i):
			continue
		else:
			New = RecurringDigits(i)[0]
			if New > Maxim:
				Maxim = New
				Num = i
			pass

	print(Num)
