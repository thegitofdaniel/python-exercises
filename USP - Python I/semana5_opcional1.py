def fizzbuzz(val):
	if (val % 3 == 0) and (val % 5 != 0):
		return 'Fizz'
	elif (val % 3 != 0) and (val % 5 == 0):
		return 'Buzz'
	elif (val % 3 == 0) and (val % 5 == 0):
		return 'FizzBuzz'
	else:
		return val