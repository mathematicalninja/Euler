# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.


def run():
	import re
	Reg = re.compile(r"1\d2\d3\d4\d5\d6\d7\d8\d9")

	Flip = 10**6
	for i in range(Flip, Flip *10):
		Three = "1" +str(i) +"30"
		Seven = "1" +str(i) +"70"

		if Reg.search(str(int(Three)**2)):
			print(Three)
		elif Reg.search(str(int(Seven)**2)):
			print(Seven)
