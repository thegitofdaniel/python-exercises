def ehprimo(x):

	counter = x - 1

	while counter > 1:
		resto = x % counter
		if resto == 0:
			return False
			break
		elif counter > 2:
			counter = counter - 1
		else:
			return True
			break

def maior_primo(n):
	counter = n
	primo = ehprimo(counter)

	while (primo == False):
		counter = counter - 1
		primo = ehprimo(counter)

	return(counter)