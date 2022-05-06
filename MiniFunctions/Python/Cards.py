from functions.Algebra import MultpieDic
from functions.Algebra import noDuplicates
from functools import total_ordering


@total_ordering
class Card:
	def __init__(self, CardString):
		self.Value = CardValue(CardString[:1])
		self.Suit = Suit(CardString[1:2])

	def __gt__(self, Other):
		if self.Value != Other.Value:
			return self.Value > Other.Value
		else:
			return self.Suit > Other.Suit

	def __eq__(self, Other):
		return (self.Value == Other.Value and self.Suit == Other.Suit)

	def write(self):
		print(self.Value.name + " of " + self.Suit.name)

	def __str__(self):
		return self.Value.Value + self.Suit.value


@total_ordering
class Suit:
	def __init__(self, Char):
		self.value = Char.upper()
		self.SuitName()

	def __eq__(self, Other):
		return self.value == Other.value

	def __gt__(self, Other):
		return self.value > Other.value

	def SuitName(self):
		if self.value == "C":
			self.name = "Clubs"
		if self.value == "D":
			self.name = "Diamonds"
		if self.value == "H":
			self.name = "Hearts"
		if self.value == "S":
			self.name = "Spades"

	def __str__(self):
		try:
			return self.name
		except:
			return "ERROR"


@total_ordering
class CardValue:
	def __init__(self, ValueString):
		self.Value = ValueString
		if ValueString in ["2", "3", "4", "5", "6", "7", "8", "9"]:
			self.Number = int(ValueString)
		else:
			self.Number = ["T", "J", "Q", "K", "A"].index(ValueString.upper()) +10
		self.NameSting()
		pass

	def __eq__(self, Other):
		return self.Number == Other.Number

	def __gt__(self, Other):
		return self.Number > Other.Number

	def NameSting(self):
		if self.Number <=10:
			self.name = str(self.Number)
		elif self.Value == "A":
			self.name = "Ace"
		elif self.Value == "K":
			self.name = "King"
		elif self.Value == "Q":
			self.name = "Queen"
		elif self.Value == "J":
			self.name = "Jack"
		else:
			self.name = "ERROR"

	def __str__(self):
		return self.name


class Hand:
	def __init__(self, CardList):
		self.Cards = sorted([Card(i) for i in CardList])
		self.Current = 0
		self.CardValues=[]
		self.GetCardValues()
		self.SuitValues = []
		self.GetSuitValues()
		pass

	def __str__(self):
		return str([str(c) for c in self.Cards])

	def __iter__(self):
		return self

	def __next__(self):
		if self.Current >= len(self.Cards):
			self.Current = 0
			raise StopIteration
		else:
			self.Current += 1
			return self.Cards[self.Current -1]

	def GetCardValues(self):
		for k in self.Cards:
			self.CardValues.append(k.Value.Number)

	def GetSuitValues(self):
		for k in self.Cards:
			self.SuitValues.append(str(k.Suit))





@total_ordering
class PokerHand(Hand):

	def __init__(self, CardList):
		super().__init__(CardList)
		self.Multiples = MultpieDic(self.CardValues)
		self.GetHandValue()
		pass

	if True:

		def GetHandValue(self):
			self.isRoyal()


		def isRoyal(self):
			if len(set(self.SuitValues))==1:
				if self.CardValues ==[10, 11, 12, 13, 14]:
					# print("Royal Flush")
					self.HandValue = [10, self.SuitValues[0]]
					self.HandType = "Royal Flush of " +str(self.SuitValues[0])
				else:
					self.isStraightFlush()
			else:
				self.isFour()
			pass

		def isStraightFlush(self):
			if len(set(self.SuitValues))==1:
				if [min(self.CardValues) +i for i in range(5)] == self.CardValues:
					# print("Straight Flush")
					self.HandValue = [9, max(self.Cards)]
					self.HandType = "Straight Flush, " +str(max(self.Cards)) +" High"
				else:
					self.isFlush()
			else:
				self.isFour()
			pass

		def isFour(self):
			if 4 in self.Multiples.values():
				# print("Four of a Kind")
				for Value, multiples in self.Multiples.items():
					if multiples == 4:
						self.HandValue = [8, Value]
						self.HandType = "Four " +str(Value)
			else:
				self.isFull()
			pass

		def isFull(self):
			if 3 in self.Multiples.values():
				if 2 in self.Multiples.values():
					# print("Full House")
					for Value, multiples in self.Multiples.items():
						if multiples == 3:
							Over = Value
					for Value, multiples in self.Multiples.items():
						if multiples == 2:
							Under = Value
					self.HandValue = [7, Over, Under]
					self.HandType = "Three " +str(Over) +" over two " +str(Under)
				else:
					self.isThree()
			else:
				self.isStraight()
			pass

		def isFlush(self):
			if len(set(self.SuitValues))==1:
				# print("Flush")
				self.HandValue = [6, self.SuitValues[0], reversed(sorted(self.Cards))]
				self.HandType = "Flush of " +str(self.SuitValues[0])
			else:
				self.isStraight()
			pass

		def isStraight(self):
			if [min(self.CardValues) +i for i in range(5)] == self.CardValues:
				# print("Straight")
				self.HandValue = [5, max(self.Cards)]
				self.HandType = "Straight " +str(max(self.CardValues)) +" High"
			else:
				self.isThree()
			pass

		def isThree(self):
			if 3 in self.Multiples.values():
				# print("Three of a Kind")
				for Value, multiples in self.Multiples.items():
					if multiples == 3:
						self.HandValue = [4, Value, list(reversed(sorted(noDuplicates(self.CardValues).keys())))]
						self.HandType = "Three " +str(Value)
				pass
			else:
				self.is2Pair()
			pass

		def is2Pair(self):
			if 2 in self.Multiples.values():
				if MultpieDic([self.Multiples[i] for i in self.Multiples])[2]==2:
					# print("Two Pair")

					for Value3, multiples3 in self.Multiples.items():
						if multiples3 == 1:
							for Value, multiples in self.Multiples.items():
								if multiples == 2:
									for Value2, multiples2 in self.Multiples.items():
										if multiples2 == 2 and Value2 != Value:
											self.HandValue = [3, max(Value, Value2), min(Value, Value2), Value3]
											self.HandType = "pair of "+ str(Value) +" and a pair of " + str(Value2)
				else:
					self.isPair()
			else:
				self.isHigh()
			pass

		def isPair(self):
			if 2 in self.Multiples.values():
				# print("Two of a Kind")
				for Value, multiples in self.Multiples.items():
					if multiples == 2:
						self.HandValue = [2, Value, list(reversed(sorted(noDuplicates(self.CardValues).keys())))]
						self.HandType = "A pair of " +str(Value)
				pass
			else:
				self.isHigh()
			pass

		def isHigh(self):
			# print("High Card")
			self.HandValue = [1, self.Cards]
			self.HandType = "High card: " +str(self.Cards)
			pass

	def __gt__(self, Other):
		return self.HandValue > Other.HandValue

	def __eq__(self, Other):
		return self.HandValue ==Other.HandValue
