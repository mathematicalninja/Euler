# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

from functions.NumbersAsWords import WordSum
from functions.Integer import Triangular


def MaxScore(Words):
	Maxim = 0
	for word in Words:
		Sum =WordSum(word)
		if Sum>Maxim:
			Maxim =Sum
	return(Maxim)


def TriMax(Maxim):
	n = 0
	while True:
		if Triangular(n +1)>Maxim:
			return(n)
			break
		n = n +1


def run():
	with open("_42\\Data_Hard.txt", "r") as File:
		Words = eval("[" +File.read() +"]")
	Smax = MaxScore(Words)
	Tmax = TriMax(Smax)

	Tris = [Triangular(n) for n in range(0, Tmax +1)]

	print(Tris)

	Count =0
	for word in Words:
		if WordSum(word) in Tris:
			print(word)
			Count = Count +1
	print(Count)
