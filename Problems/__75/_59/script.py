# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.


def run():
	# ran SecondLoop, got the Gospel of Joh, Code "god" [103,111,100]
	Code = [103, 111, 100]
	with open(r"_59\Data_Hard.txt", "r") as File:
		Data = eval("[" +File.read() +"]")

	Sum = 0
	for index in range(len(Data)):
		Val = Data[index] ^ Code[index %3]
		Sum = Sum + Val
		pass
	print(Sum)

	pass


def SecondLoop():
	# ran QuickLoop and got [[103, 104, 113], [103, 111, 100]] as Likely
	Codes = [[103, 104, 113], [103, 111, 100]]
	with open(r"_59\Data_Hard.txt", "r") as File:
		Data = eval("[" +File.read() +"]")

	for Code in Codes:
		OutData = ""
		for index in range(len(Data)):
			Val = Data[index] ^ Code[index %3]
			OutData = OutData + chr(Val)
			pass
		print(OutData)


	pass


def QuickLoop():
	import re
	Likely = []
	TheReg = re.compile(r"\s[aA]\s|\s[Tt]he\s")
	with open(r"_59\Data_Hard.txt", "r") as File:
		Data = eval("[" +File.read() +"]")
	for i in range(26):
		for j in range(26):
			for k in range(26):
				Code = [97 +i, 97 +j, 97 +k]
				OutData = ""
				for index in range(len(Data)):
					Val = Data[index] ^ Code[index %3]
					OutData = OutData + chr(Val)
					pass
				if TheReg.search(OutData):
					Likely.append(Code)
	print(Likely)

	pass
