def soma_lista(lista):

	if len(lista) > 1:

		return lista[0] + soma_lista(lista[1:])

	else:

		return lista[0] 

def encontra_impares(lista):


	if len(lista) > 1:

		if (lista[0] % 2) == 0:

			return encontra_impares(lista[1:])

		else:

			return [lista[0]] + encontra_impares(lista[1:])

	else:

		if (lista[0] % 2) == 0:

			return []

		else:
			return [lista[0]]


def incomodam(n):
	if n > 0:
		return ("incomodam "+incomodam(n-1))
	else:
		return ""

def elefantes(n):

	if n == 1:
		return("Um elefante incomoda muita gente")

	elif n>1:

		return(str(elefantes(n-1)) + "\n" + (str(n)+" elefantes "+incomodam(n)+"muito mais") + "\n" + str(n)+" elefantes "+incomodam(n)+"muita gente")

	else:
		return("")