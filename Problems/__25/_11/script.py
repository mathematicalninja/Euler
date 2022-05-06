# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


def install():
	import re
	NumberPair = re.compile(r"\s*(\d\d)\s*")

	with open("_11\\Data.txt", "r") as Data:
		GridLinesText = Data.readlines()

	Grid = []

	for Line in GridLinesText:
		Grid.append(NumberPair.findall(Line))

	with open("_11\\DataGrid.py", "w") as File:
		File.write(str(Grid))


def MaxProd(Grid, Adjacent):
	from functions.GridProperties import GridScan

	Full = GridScan(Grid, Adjacent)
	Products = []
	for Tuple in Full:
		Product = 1
		for k in Tuple:
			Product = Product *int(k)
		Products.append(Product)
	return max(Products)


def run():
	with open("_11\\DataGrid.py", "r") as File:
		Data=eval(File.read())

	print(MaxProd(Data, 4))
