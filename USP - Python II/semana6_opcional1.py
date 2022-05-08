def fatorial(x):
	if x <= 1:
		return 1

	else:
		return x * fatorial(x-1)

def fibonacci(n):
	if n <=2:
		return 1

	else:
		return fibonacci(n-1) + fibonacci(n-2)