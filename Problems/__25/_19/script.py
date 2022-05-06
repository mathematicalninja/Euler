# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

NormMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LeapMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

Days = [
    "Mon",
    "Tue",
    "Wed",
    "Thur",
    "Fri",
    "Sat",
    "Sun",
]

FirstDay = 0
SecondDay = 1


def IsLeapYear(YEAR):
	if YEAR % 4!=0:
		return False
	elif YEAR % 400==0:
		return True
	elif YEAR % 100==0:
		return False
	else:
		return True


YearStart = {1900: 0}

FirstDays = {}


def run():
	for Year in range(1900, 2001):
		if IsLeapYear(Year):
			YearStart[Year +1] = (YearStart[Year] +2) %7
		else:
			YearStart[Year +1] = (YearStart[Year] +1) %7

	for Year in range(1900, 2001):
		Result = [YearStart[Year]]
		if IsLeapYear(Year):
			Twiddle=LeapMonths
		else:
			Twiddle=NormMonths
		for month in range(len(Twiddle) -1):
			Result.append((Result[month] +Twiddle[month]) %7)
		FirstDays[Year]=Result

	count = 0
	for Year, Months in FirstDays.items():
		if Year == 1900:
			continue
		for month in Months:
			if month ==6:
				count = count +1
	print(count)
