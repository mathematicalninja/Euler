# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# Straight Flush: All cards are consecutive values of same suit.
# Four of a Kind: Four cards of the same value.
# Full House: Three of a kind and a pair.
# Flush: All cards of the same suit.
# Straight: All cards are consecutive values.
# Three of a Kind: Three cards of the same value.
# Two Pairs: Two different pairs.
# One Pair: Two cards of the same value.
# High Card: Highest value card.
#
# How many hands does Player 1 win?
from functions.Algebra import MultpieDic

from functions.Cards import Card
from functions.Cards import Hand
from functions.Cards import PokerHand

Hands = ["2S 2S 2H KS KS QD QH QS TD 2S"]

TestHands = [
    "AS KS QS JS TS",  # Royal Flush
    "KS QS JS TS 9S",  # Straight Flush
    "KS KH KC KD QS",  # Four of a Kind
    "KS KH KC QD QS",  # Full House
    "QS AS 3S TS 4S",  # Flush
    "AS KS QS JS TD",  # Straight
    "KS KH KC QD TS",  # Three of a Kind
    "KS KH QC QD TS",  # Two Pair
    "KS KH QC 6D TS",  # Two of a Kind
    "KS 2H QC 6D TS"  # High Card
]


def run():
	# Hands = Tests()
	# print(Hands)
	Hands = install()

	Sum = 0
	for String in Hands:
		Hand1, Hand2 = SplitHands(String)
		Sum += (Hand1>Hand2)
		if Hand1.HandValue[0] == Hand2.HandValue[0]:
			print(Hand1)
			print(Hand2)
	print(Sum)
	# TestHandsData = [PokerHand(HStr.split(" ")) for HStr in TestHands]


def install():
	import re
	with open("_54\\Data_Hard.txt", "r") as File:
		Data = File.readlines()

	newReg = re.compile(r"\\n")
	for line in Data:
		if newReg.search(line) is not None:
			newReg.sub(repl="", string=line)

	return Data


def SplitHands(HandString):
	Left = HandString[:14]
	Right = HandString[15:]
	Hand1 = PokerHand(Left.split(" "))
	Hand2 = PokerHand(Right.split(" "))
	return [Hand1, Hand2]




def Tests():
	Lines = STR.splitlines()
	for ind in reversed(range(len(Lines))):
		if Lines[ind]=="":
			del Lines[ind]
	return Lines
	pass


STR = r"""
5H 5C 6S 7S KD 2C 3S 8S 8D TD
5D 8C 9S JS AC 2C 5C 7D 8S QH
2D 9C AS AH AC 3D 6D 7D TD QD
4D 6S 9H QH QC 3D 6D 7H QD QS
2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
"""
