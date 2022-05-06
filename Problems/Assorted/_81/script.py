# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

from functions.Integer import PairSum


def run():


	Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	R1 = [131, 201, 630, 537, 805]
	R2 = [673, 96, 803, 699, 732]
	R3 = [234, 342, 746, 497, 524]
	R4 = [103, 965, 422, 121, 37]
	R5 = [18, 150, 111, 956, 331]
	Matrix = [R1, R2, R3, R4, R5]
	Matrix = initiate()

	Ans = MatrixDiagonal(Matrix)
	print(Ans[0][0])
	print(Ans)


	pass


def MatrixDiagonal(Matrix):
	Clone = [[0 for i in j] for j in Matrix]
	MatrixSumCap = len(Matrix) +len(Matrix[0])
	for Diag in reversed(range(MatrixSumCap)):
		for IndexPair in PairSum(Diag, [len(Matrix[0]), len(Matrix)]):
			try:
				Down = Clone[IndexPair[1]][IndexPair[0] +1]
			except:
				Down = -1
			try:
				Right = Clone[IndexPair[1] +1][IndexPair[0]]
			except:
				Right = -1
			if min(Right, Down) == -1:
				Adder = max(max(Right, Down), 0)
			else:
				Adder = min(Right, Down)

			Clone[IndexPair[1]][IndexPair[0]] = Matrix[IndexPair[1]][IndexPair[0]] +Adder
	return Clone


def initiate():
	Matrix = []
	with open("_81\\Data_Hard.txt", "r") as File:
		for Line in File.readlines():
			Matrix.append(eval("[" +Line +"]"))
		pass
	pass
	return Matrix
