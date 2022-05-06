# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# numbers = [
#     "a",
#     "b",
#     "c",
#    	"d",
#    	"e",
#    	"f",
#    	"g",
#    	"h"
# ]


def run():
	Max = 10
	numbers = []
	for i in range(0, Max):
		numbers.append(str(i))
	Permutes = [""]
	while True:
		Temp =[]
		if len(Permutes[0])==Max:
			break
		for perm in Permutes:
			for d in numbers:
				if d in perm:
					continue
				else:
					Temp.append(perm +d)
		Permutes = Temp
	print(sorted(Permutes)[1000000 -1])
