# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Which starting number, under one million, produces the longest chain?


def CheckedCollatzSequence(Integer, Checked={1: 1}):


	def ColatzStep(Integer):
		if Integer % 2 == 0:
			return int(Integer /2)
		else:
			return 3 * Integer +1


	def CollatzAddSeq(seq, Checked):
		CurrentValue = 1
		for n in reversed(seq):
			if n in Checked:
				if type(Checked[n]) is int:
					CurrentValue = Checked[n]
				else:
					Checked[n] = CurrentValue
			else:
				Checked[n] = CurrentValue
			CurrentValue = CurrentValue +1
		pass




	Sequence = [Integer]
	while True:
		if Integer <=1:
			break
		else:
			if Integer in Checked.keys():
				break
			else:
				Checked[Integer] = True
			Integer = ColatzStep(Integer)
			Sequence.append(int(Integer))
	CollatzAddSeq(seq=Sequence, Checked=Checked)
	return Checked




def LongestChain(Integer):
	Maxim=1
	Value=1
	checked={1: 1}
	for i in range(1, Integer +1):
		checked = CheckedCollatzSequence(i, checked)
	return(checked)


def run():
	LC = LongestChain(1000000)
	Maxim = 0
	Number = 0
	for key, value in LC.items():
		if value >Maxim:
			Maxim = value
			Number = key
	print(Number, Maxim)
	pass
