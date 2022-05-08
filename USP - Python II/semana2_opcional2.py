def primeiro_lex(lista):

	aux = lista[0]

	for nome in lista:

		for i in range(len(nome)):
			if nome[i] == aux[i]:
				pass
			elif ord(nome[i]) > ord(aux[i]):
				break
			else:
				aux = nome

	return(aux)