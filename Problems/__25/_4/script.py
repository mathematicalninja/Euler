# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def LargestPalindrome(LargestFactor):
	from functions.Integer import IsPalindrome

	Palnidromes = []

	for i in range(1, LargestFactor +1):
		for j in range(1, LargestFactor +1):
			if IsPalindrome(i *j):
				if i *j in Palnidromes:
					continue
				else:
					Palnidromes.append(i *j)
	return max(Palnidromes)
	pass


if __name__ == "__main__":
	print(LargestPalindrome(999))
