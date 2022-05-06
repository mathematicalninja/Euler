# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

from functions.Integer import IsPythagorean
from functions.Integer import PySumTo





def run():
	Maxim = 1000
	Best=[]
	for per in range(3, Maxim +1):
		Trips = (PySumTo(per))
		if len(Trips)>len(Best):
			Best = Trips
			print(Best)
			print(len(Best))
			print(sum(Best[0]))
	pass
