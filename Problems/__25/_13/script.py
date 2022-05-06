
def install():
	with open("_13\\Data.txt", "r") as File:
		Data = File.readlines()
	Numbers = []
	for i in Data:
		Numbers.append(int(i))

	k = sum(Numbers)
	print(k)

	print(str(k)[0:10])


def run():
	install()
