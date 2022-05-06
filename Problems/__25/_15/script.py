# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?


def run():
	# it's pascal triangle, middle of line 41:
	# 40!
	# 20! * 20!
	#
	#  39  37  7  33  31  29    5  23    2^2

	print(39 *37 *33 *31 *29 *23 *7 *5 *2 *2)
