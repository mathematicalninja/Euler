# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?

from functions.Integer import BiggestCoin


def run():
	print(BiggestCoin(Value=100, Coins=list(range(99, 1 -1, -1))))
	pass

# 190569291
