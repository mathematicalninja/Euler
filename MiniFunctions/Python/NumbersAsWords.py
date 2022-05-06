

def WordSum(Name):
	from functions.NumbersAsWords import LettersVals
	Sum = 0
	for letter in Name:
		Sum = Sum +LettersVals[letter.lower()]
	return Sum


def IntToStr(Integer):

	def FullHundred(IntOrStr):
		INT = int(IntOrStr)
		STR = str(IntOrStr)
		if INT>= 100:
			return hundredString(INT)
		else:
			return TensStrings(INT)
		pass


	def hundredString(IntToStr):
		INT = int(IntToStr)
		STR = str(IntToStr)
		Hun = int(STR[0])
		Ten = STR[1:3]

		if int(Ten)==0:
			return units[Hun]+ " hundred"
		else:
			return units[Hun]+ " hundred"+ " and " + TensStrings(Ten)


	def TensStrings(intOrStr):
		INT = int(intOrStr)
		STR = str(intOrStr)

		if INT>= 20:
			Str = str(INT)
			Ten = tens[int(STR[0])]
			Unit = units[int(STR[1])]
			return Ten + " " +Unit
			pass
		elif INT>= 10:
			return dozens[INT]
		else:
			return units[INT]
		pass


	tens ={
	    2: "twenty",
	    3: "thirty",
	    4: "forty",
	    5: "fifty",
	    6: "sixty",
	    7: "seventy",
	    8: "eighty",
	    9: "ninety"
	}

	dozens = {
	    10: "ten",
	    11: "eleven",
	    12: "twelve",
	    13: "thirteen",
	    14: "fourteen",
	    15: "fifteen",
	    16: "sixteen",
	    17: "seventeen",
	    18: "eighteen",
	    19: "nineteen"
	}

	units = {0: "",
	         1: "one",
	         2: "two",
	         3: "three",
	         4: "four",
	         5: "five",
	         6: "six",
	         7: "seven",
	         8: "eight",
	         9: "nine"
	         }



	if Integer>= 1000:
		STR = str(Integer)
		if Integer % 1000 !=0:
			return FullHundred(STR[:-3])+ " thousand " +FullHundred(STR[-3:])
		else:
			return FullHundred(STR[:-3])+ " thousand"

	else:
		return FullHundred(Integer)
	pass
