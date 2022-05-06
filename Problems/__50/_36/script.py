# The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from functions.Integer import IsPalindrome


def run():
	Maxim = 1000000
	Palies = []
	for n in range(1, Maxim):
		if n %2==0:
			continue
		if n %10==0:
			continue
		if IsPalindrome(n):
			if IsPalindrome(bin(n)[2:]):
				Palies.append(n)
	print(Palies)
	print(sum(Palies))
	pass
