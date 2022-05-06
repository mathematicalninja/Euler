# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

from functions.Integer import DigitCount


def run():
	Maxim = 22
	Count = 0
	Succs = []
	for Pow in range(Maxim):
		for k in range(1, 9 +1):
			if DigitCount(k**Pow) == Pow:
				Count = Count +1
				Succs.append([k, Pow])
	print(Count)
	print(Succs)
	pass



def OldRun():


	Maxim = 150
	Count = 0
	Minim = 0
	for Pow in range(1, Maxim):
		Succ = False
		for k in range(Minim, 9 +1):
			Length = DigitCount(k**Pow)
			# print(Pow, k, Length)
			if Length == Pow:
				Count = Count + 1
				# print(True)
				# print(Count, k, Pow, k**Pow)
				# print(k**Pow)
				Succ = True
			elif Length >Pow:
				# print(False)
				Succ = True
				# print(Succ)
				break
			elif k ==9:
				Succ = True
				break
			if Pow>1:
				Minim = Minim +1
				break
			elif Pow in [0, 1]:
				Succ =True
				continue
			print(k, Pow, Succ, Minim)
		if not Succ:
			if Pow>1:
				print("done")
				break
		if Minim >9:
			print(Minim)
			break
		print(Count)
		pass
