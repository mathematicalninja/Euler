# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# from functions.Integer import IsPerfect
from functions.Integer import FactorsOf


def IsAbundant(Integer):
	return (sum(FactorsOf(Integer))>2 *Integer)


def LazyAbunds(Abundants):
	Output = []
	for n in range(len(Abundants)):
		for m in Abundants[n:]:
			# if(n +m not in Output):
			Output.append(Abundants[n] +m)
	return dict.fromkeys(Output)



def GetAbundants(Integer):
	Abundants=[]
	for i in range(1, Integer +1):
		if IsAbundant(i):
			Abundants.append(i)
	return Abundants


def LazySum(Fails, Maximum=28123):
	Sum = 0
	Success = []
	for i in range(1, Maximum):
		if i in Fails:
			del Fails[i]
		else:
			Success.append(i)
		pass
	return sum(Success)


def run():
	Abundants = GetAbundants(28123)
	Fails = LazyAbunds(Abundants)
	print(LazySum(Fails, 28123))
